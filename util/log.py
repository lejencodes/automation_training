import os
import time
import logging



class LogMessage:
    def __init__(self):
        title = u'Test Result'
        day = time.strftime("%Y%m%d%H", time.localtime(time.time()))
        file = os.path.join(os.getcwd(), 'logs', f'{day}.log')
        self.logger = logging.Logger(title)
        self.logger.setLevel(logging.INFO)
        self.logfile = logging.FileHandler(file)
        self.logfile.setLevel(logging.INFO)
        self.control = logging.StreamHandler()
        self.control.setLevel(logging.INFO)
        self.formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.logfile.setFormatter(self.formater)
        self.control.setFormatter(self.formater)
        self.logger.addHandler(self.logfile)
        self.logger.addHandler(self.control)

    def debugInfo(self, message):
        self.logger.debug(message)

    def info_log(self, message):
        self.logger.info(message)

    def warn_log(self, message):
        self.logger.warn(message)

    def error_log(self, message):
        self.logger.error(message)
