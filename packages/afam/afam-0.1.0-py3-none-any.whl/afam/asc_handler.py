"""
    This module provides a class to handle .asc-files in python
"""

from .asc_dataclasses import ASC_BUTTON
from .asc_dataclasses import ASC_MSG
from .asc_dataclasses import ASC_SSACC
from .asc_dataclasses import ASC_SFIX
from .asc_dataclasses import ASC_EBLINK
from .asc_dataclasses import ASC_EFIX
from .asc_dataclasses import ASC_ESACC
from .asc_dataclasses import ASC_INPUT
from .asc_dataclasses import ASC_SBLINK


class ASC_File_Handler():
    """
    A class used to handle the parsing of an ASC file.

    Attributes
    ----------
    `info` : str
        a list of all the information in the current cutted line of the ASC file
    `id` : int
        the current trial id (used to parse the correct id to each message)
    """
    def __init__(self, id=-1, info=None, search=[]):
        self.id = id
        self.info = info
        self.search = search

# ----------------------------------------------------------------------------------------------- #

    def parse(self, token, info):
        """
        Parses one line of the ASC file.

        Parameters
        ----------
        `token` : str
            name of a specific event
        `info` : str
            information of a specific event

        Return
        ------
        `x` : object
            an event object with the processed information
        """
        self.info = info
        x = getattr(self, 'case_{}'.format(token), lambda: None)()
        return x

# ----------------------------------------------------------------------------------------------- #

    def case_BUTTON(self):
        """
        Returns a created BUTTON event object

        Return
        ------
        object
            a BUTTON event object
        """
        try:
            return ASC_BUTTON(id=self.id,
                              t=int(self.info[0]),
                              b=int(self.info[1]),
                              s=int(self.info[2]))
        except ValueError:
            print("COULD NOT CONVERT TEXTLINE: BUTTON {}".format(' '.join(self.info)))
            pass

# ----------------------------------------------------------------------------------------------- #

    def case_INPUT(self):
        """
        Returns a created input event object

        Return
        ------
        object
            a INPUT event object
        """
        try:
            return ASC_INPUT(id=self.id, t=int(self.info[0]), p=int(self.info[1]))
        except ValueError:
            print("COULD NOT CONVERT TEXTLINE: INPUT {}".format(' '.join(self.info)))
            pass

# ----------------------------------------------------------------------------------------------- #

    def case_SBLINK(self):
        """
        Returns a created SBLINK event object

        Return
        ------
        object
            a SBLINK event object
        """
        try:
            return ASC_SBLINK(id=self.id, eye=self.info[0], st=int(self.info[1]))
        except ValueError:
            print("COULD NOT CONVERT TEXTLINE: SBLINK {}".format(' '.join(self.info)))
            pass

# ----------------------------------------------------------------------------------------------- #

    def case_SSACC(self):
        """
        Returns a created SSACC event object

        Return
        ------
        object
            a SSACC event object
        """
        try:
            return ASC_SSACC(id=self.id, eye=self.info[0], st=int(self.info[1]))
        except ValueError:
            print("COULD NOT CONVERT TEXTLINE: SSACC {}".format(' '.join(self.info)))
            pass

# ----------------------------------------------------------------------------------------------- #

    def case_SFIX(self):
        """
        Returns a created SFIX event object

        Return
        ------
        object
            a SFIX event object
        """
        try:
            return ASC_SFIX(id=self.id, eye=self.info[0], st=int(self.info[1]))
        except ValueError:
            print("COULD NOT CONVERT TEXTLINE: SFIX {}".format(' '.join(self.info)))
            pass

# ----------------------------------------------------------------------------------------------- #

    def case_EBLINK(self):
        """
        Returns a created EBLINK event object

        Return
        ------
        object
            a EBLINK event object
        """
        try:
            return ASC_EBLINK(id=self.id,
                              eye=self.info[0],
                              st=int(self.info[1]),
                              et=int(self.info[2]),
                              d=int(self.info[3]))
        except ValueError:
            print("COULD NOT CONVERT TEXTLINE: EBLINK {}".format(' '.join(self.info)))
            pass

# ----------------------------------------------------------------------------------------------- #

    def case_ESACC(self):
        """
        Returns a created ESACC event object

        Return
        ------
        object
            a ESACC event object
        """
        try:
            return ASC_ESACC(id=self.id,
                             eye=self.info[0],
                             st=int(self.info[1]),
                             et=int(self.info[2]),
                             d=int(self.info[3]),
                             sx=float(self.info[4]),
                             sy=float(self.info[5]),
                             ex=float(self.info[6]),
                             ey=float(self.info[7]),
                             ampl=float(self.info[8]),
                             pvel=float(self.info[9]),
                             resx=None,             # TODO resx
                             resy=None)             # TODO resy
        except ValueError:
            print("COULD NOT CONVERT TEXTLINE: ESACC {}".format(' '.join(self.info)))
            pass

# ----------------------------------------------------------------------------------------------- #

    def case_EFIX(self):
        """
        Returns a created EFIX event object

        Return
        ------
        object
            a EFIX event object
        """
        try:
            return ASC_EFIX(id=self.id,
                            eye=self.info[0],
                            st=int(self.info[1]),
                            et=int(self.info[2]),
                            d=int(self.info[3]),
                            x=float(self.info[4]),
                            y=float(self.info[5]),
                            resx=None,             # TODO resx
                            resy=None)             # TODO resy
        except ValueError:
            print("COULD NOT CONVERT TEXTLINE: EFIX {}".format(' '.join(self.info)))
            pass

# ----------------------------------------------------------------------------------------------- #

    def case_MSG(self):
        """
        Returns a created MSG event object

        Return
        ------
        object
            a MSG event object
        """
        try:
            st = int(self.info.pop(0))
            if self.info[0] == 'SYNCTIME':
                return ASC_MSG(id=self.id, t=self.info.pop(0), st=st, data=" ".join(self.info))
            elif self.info[0] == 'TRIALID':
                self.id = int(self.info[1])
                return ASC_MSG(id=self.id, t=self.info.pop(0), st=st, data=" ".join(self.info))
            elif self.info[0] == 'TRIAL':  # TODO Change to TRIAL_RESULT
                msg = ASC_MSG(id=self.id, t=self.info.pop(0), st=st, data=" ".join(self.info))
                self.id = -1
                return msg
            elif self.info[0] in self.search:
                return ASC_MSG(id=self.id, t=self.info.pop(0), st=st, data=" ".join(self.info))
            else:
                return ASC_MSG(id=self.id, t=None, st=st, data=" ".join(self.info))
        except ValueError:
            print("COULD NOT CONVERT TEXTLINE: MSG {}".format(' '.join(self.info)))
            pass

# ----------------------------------------------------------------------------------------------- #

    def read_asc_file(self, path):
        """
        Reads the given ASC file and returns a list with all eye events

        Parameter
        ---------
        `path` : str
            The file path of the ASC file

        Return
        ------
        `event_list` : list
            a list of all eye events
        """
        event_list = []
        with open(path) as fp:
            line = fp.readline()
            while line:
                cutted_line = ' '.join(line.split()).split(' ')
                e = self.parse(cutted_line.pop(0), cutted_line)
                if e:
                    event_list.append(e)
                line = fp.readline()
        return event_list
