import logging
from logging import handlers
from pathlib import Path


class AORunActivityLog:
    """
    Class to support activity and runtime logs
    """

    _prefix: str
    _home: str
    _run_descriptor: str
    _activity_descriptor: str
    _runtime_logger: logging
    _activity_logger: logging

    def __init__(self, prefix: str, home: str = ".", run_descriptor: str = "runtime",
                 activity_descriptor: str = "activity"):
        """
        Initializes logging structures. Sets logging to home/prefix-(run-descriptor|log_descriptor).log
        :param prefix: the activity being logged
        :param home: the directory to contain (or which contains) the log file
        :param run_descriptor: suffix of runtime file log (mirrors console)
        :param activity_descriptor: suffix of activity log
        """
        # use fields here. Their setters call reset()
        self._prefix = prefix
        self._home = home
        self._run_descriptor = run_descriptor
        self._activity_descriptor = activity_descriptor
        self.reset()

    def reset(self):
        """
        Resets file logging to allow for changed descriptors
        :return:
        """
        logging.basicConfig(level=logging.INFO)
        # logging.getLogger("paramiko").setLevel(logging.ERROR)

        # Each individual run is not important, so accumulate them in a log
        instance_id_log_path = f"{self.prefix}-{self.run_descriptor}.log"

        basic_formatter = logging.Formatter(fmt='%(asctime)s:%(levelname)s:%(message)s', datefmt='%m-%d %H:%M')
        # More time, fewer other details in activity
        activity_formatter = logging.Formatter(fmt='%(asctime)s:%(message)s', datefmt='%m-%d-%Y %H-%M-%S')

        # will this just get the root logger?
        self.runtime_logger = logging.getLogger()
        # runtime_logger = logging.getLogger(run_logger_name)
        # add a console handler to the runtime logger
        # Not needed - the console is where the root logger goes.
        # console = logging.StreamHandler()
        # console.setFormatter(basic_formatter)
        #    runtime_logger.addHandler(console)

        file_handler = handlers.RotatingFileHandler(Path(self._home, instance_id_log_path), maxBytes=4096000,
                                                    backupCount=100)

        # file_handler = logging.FileHandler(Path(log_root, f"{instance_id_log_path}"))
        file_handler.setFormatter(basic_formatter)
        self.runtime_logger.addHandler(file_handler)

        self.activity_logger = logging.getLogger('activity')
        # Dont rotate file
        activity_file_handler = logging.FileHandler(Path(self.home, f"{self.prefix}-{self.activity_descriptor}.log"))
        activity_file_handler.setLevel(logging.INFO)
        activity_file_handler.setFormatter(activity_formatter)
        self.activity_logger.addHandler(activity_file_handler)

    @property
    def prefix(self):
        return self._prefix

    @prefix.setter
    def prefix(self, value):
        self._prefix = value
        self.reset()

    @property
    def home(self):
        return self._home

    @home.setter
    def home(self, value):
        self._home = value
        self.reset()

    @property
    def run_descriptor(self):
        return self._run_descriptor

    @run_descriptor.setter
    def run_descriptor(self, value):
        self._run_descriptor = value
        self.reset()

    @property
    def activity_descriptor(self):
        return self.activity_descriptor

    @activity_descriptor.setter
    def activity_descriptor(self, value):
        self.activity_descriptor = value
        self.reset()

    @property
    def runtime_logger(self):
        return self._runtime_logger

    _activity_logger: logging

    @runtime_logger.setter
    def runtime_logger(self, value):
        self._runtime_logger = value

    @property
    def activity_logger(self):
        return self._activity_logger

    @activity_logger.setter
    def activity_logger(self, value):
        self._activity_logger = value
