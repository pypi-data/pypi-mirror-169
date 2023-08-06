import os
from datetime import datetime
from ngtextpreprocess.global_params import curr_directory


class MakeDirectory:
    """
        This class is used for automatic creation of a directory structure.
    """

    def __init__(self, dir_structure=None, basefolder=None, file_start=None):
        # for creating a directory using a single path.
        self.dir_structure = dir_structure 
        # for creating a directory using separate folder and file name.
        self.basefolder = basefolder
        self.file_start = file_start
        self.curr_year = datetime.now().strftime("%Y")
        self.curr_month = datetime.now().strftime("%m")
        self.curr_day = datetime.now().strftime("%d")
        self.date = datetime.now().date()
        self.hour = datetime.now().strftime("%H")
        self.mins = datetime.now().strftime("%M")
        self.sec = datetime.now().strftime("%S")
        self.time = "{}-{}-{}".format(
            self.hour,
            self.mins,
            self.sec
        )

    def create_logging_file(self):
        """
            Creates a logging directory structure

            :param self: Inherited from class attributes
            :return: Logging directory path
            :rtype: str
        """
        try:
            # creating custom folder path
            fold_path = "{}\\{}\\{}\\{}".format(
                self.basefolder, 
                self.curr_year, 
                self.curr_month, 
                self.curr_day)

            # creating absolute path
            logfold_name = os.path.join(curr_directory, fold_path)

            # creating the final directory structure
            if not os.path.exists(logfold_name):
                os.makedirs(logfold_name)

            # generating the logging file name
            log_txt = f"{logfold_name}" + "{}_{}_{}.txt".format(
                self.file_start, 
                self.date,
                self.time)
            return log_txt
        except Exception as e:
            return f"Couldn't create log file: \n{str(e)}"
