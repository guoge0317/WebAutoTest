import os
import time
import logging


path = os.getcwd()


class Log:
    def __init__(self):
        title = u'注册测试'
        day = time.strftime("%Y%m%d%H", time.localtime(time.time()))
        pad = os.getcwd()
        file_dir = pad + '\\log'
        file = os.path.join(file_dir, (day + '.log'))
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

    def debugInfo(self, msg):
        self.logger.debug(msg)

    def info_log(self, msg):
        self.logger.info(msg)

    def ware_log(self, msg):
        self.logger.warning(m)

    def error_log(self, msg):
        self.logger.error(msg)
