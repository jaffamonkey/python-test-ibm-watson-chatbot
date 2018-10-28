# IMPORTS
from ansi.colour import fg, bg
from ansi.colour.fx import reset

# CONSTANTS
LOG_LEVELS = {
    "NONE": 0,
    "ERROR": 1,
    "INFO": 2,
    "DEBUG": 3
}

# COMPONENT
class Logger:

    # LOG_THRESHOLD = 0  # Silent
    LOG_THRESHOLD = 3

    @staticmethod
    def log(log_type, log_message):

        log_message = str(log_message)  # force to string

        log_level = LOG_LEVELS.get(log_type, 0)
        if log_level <= Logger.LOG_THRESHOLD:
            if log_type == "ERROR":
                print(fg.red(log_message))
            elif log_type == "DEBUG":
                print(fg.orange(log_message))
            elif log_type == "INFO":
                print(fg.blue(log_message))
            else:
                print(log_message)

    @staticmethod
    def log_pass(log_message):
        log_message = str(log_message)  # force to string
        print(fg.green(log_message))

    @staticmethod
    def log_fail(log_message):
        log_message = str(log_message)  # force to string
        print(fg.red(log_message))
