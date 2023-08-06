"""Slightly biased MITgcm telegram bot"""

import glob
import os
import subprocess
from f90nml import Parser

from .handler import Handler


class MITgcmDataParser(Parser):
    """Parser for MITgcm data files."""

    def __init__(self):
        super().__init__()
        self.comment_tokens += '#'
        self.end_comma = True
        self.indent = " "
        self.column_width = 72
        self.sparse_arrays = True


def get_parameter(datafile, keyword):
    """
    Function to parse the MITgcm 'data' file and return the parameter values
    of the given specific keyword.

    Parameters
    ----------
    datafile: string
        Full path to the MITgcm data file.
    keyword: string
        Parameter of which the value is required.

    Returns
    ----------
    value: string
        The value associated with the given keyword is returned as a string (!).
    """

    if not os.path.isfile(datafile):
        raise FileNotFoundError("could not find the datafile.")

    parser = MITgcmDataParser()
    data = parser.read(datafile)

    for section in data:
        for key, val in data[section].items():
            if key.lower() == keyword.lower():
                return val

    raise KeyError("Keyword not found")


class MITgcmHandler(Handler):
    """Handler for a MITgcm simulation."""
    # convert_script = ['convert_to_gcmt']
    convert_script = ['sbatch', 'exorad_convert']

    def setup(self):
        if "run" not in os.listdir(self.directory):
            raise FileNotFoundError("Your current working directory needs to contain a run directory")

        self.run_dir = os.path.join(self.directory, "run")

        if "input" not in os.listdir(self.directory):
            raise FileNotFoundError("Your current working directory needs to contain an input directory")

        if "data" not in os.listdir(os.path.join(self.directory, "input")):
            raise FileNotFoundError("You need a data file inside your input directory")

        self.datafile = os.path.join(os.path.join(os.getcwd(), "input"), "data")

    def _add_subscribtions(self):
        """Subscribe to the different events."""
        self._subscribe(f'(?i)status {self.directory_name}', self.respond_status)
        self._subscribe(f'(?i)progress {self.directory_name}', self.respond_progress)
        self._subscribe(f'(?i)error {self.directory_name}', self.respond_error)
        self._subscribe(f'(?i)convert {self.directory_name}', self.respond_convert)
        self._subscribe(f'(?i)status all', self.respond_status)
        self._subscribe(f'(?i)progress all', self.respond_progress)
        self._subscribe(f'(?i)error all', self.respond_error)
        self._subscribe(f'(?i)convert all', self.respond_convert)
        self._subscribe(f'(?i)list', self.respond_all)

    async def respond_all(self, event):
        """Answer the directory name upon asking for a list of active simulations."""
        return await event.respond(f"{self.directory_name}")

    async def respond_progress(self, event):
        """Answer the progress of this simulation."""
        return await event.respond(f"{self.directory_name}:\nWe are at {self.progress}%.")

    async def respond_error(self, event):
        """Answer the errors that are in the STDERR.* files."""
        errors = f"{self.directory_name}:\n"
        len_0 = len(errors)    # save string length
        for stderr in glob.glob(os.path.join(self.run_dir, "STDERR.*")):
            with open(stderr, "r") as stderr_f:
                for line in stderr_f:
                    errors += f"{line}\n" if "INI_PARMS" not in line else ""

        if len(errors) == len_0:
            return await event.respond(f"{self.directory_name}:\nNo errors yet.")

        return await event.respond(f"{self.directory_name}:\nWe got the following errors:\n{errors}")

    async def respond_convert(self, event):
        """Answer the errors that are in the STDERR.* files."""
        import subprocess
        try:
            subprocess.run(self.convert_script, check=True)
            return await event.respond(f"{self.directory_name}:\n converting")
        except subprocess.CalledProcessError:
            return await event.respond(f"{self.directory_name}:\n error when executing conversion.")

    async def respond_status(self, event):
        """Answer a status update."""
        last_iter = self.last_iter
        if not last_iter:
            return await event.respond(f"{self.directory_name}:\nNo outputs yet.")

        return await event.respond(
            "{}:\nHighest iteration is {:d} which translates to {:.1f} days.".format(self.directory_name, last_iter, self.last_day))

    @property
    def last_day(self):
        """Return the time (in days) of current snapshot."""
        deltat = int(get_parameter(self.datafile, "deltat"))
        return deltat * self.last_iter / 3600 / 24

    @property
    def last_iter(self):
        """Return the iterationnumber of current snapshot."""
        iters = [int(file.split(".")[1]) for file in glob.glob(os.path.join(self.run_dir, "T.*.meta"))]
        if bool(iters):
            return max(iters)

    @property
    def progress(self):
        """Return the progress of the simulation (in percent)."""
        nIter0 = int(get_parameter(self.datafile, "nIter0"))
        nTimeSteps = int(get_parameter(self.datafile, "nTimeSteps"))
        if bool(self.last_iter):
            return (self.last_iter - nIter0) / nTimeSteps * 100
        else:
            return 0.0