import logging.config
from datetime import datetime

class Logging():
    def __init__(self, config_path='config/logging.conf', log_path='log'):
        self.config_path = config_path
        self.log_path = log_path

        logging.config.fileConfig(self.config_path)
        self.logger = logging.getLogger('Kiwoom')
        self.kiwoom_log()

    #로그설정
    def kiwoom_log(self):
        fh = logging.FileHandler(self.log_path+'/{:%Y-%m-%d}.log'.format(datetime.now()), encoding="utf-8")
        formatter = logging.Formatter('[%(asctime)s] I %(filename)s | %(name)s-%(funcName)s-%(lineno)04d I %(levelname)-8s > %(message)s')

        fh.setFormatter(formatter)
        self.logger.addHandler(fh)