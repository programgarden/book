import logging.config
from datetime import datetime

class Logging():
    def __init__(self, config_path='config/logging.conf', log_path='log'):
        self.config_path = config_path
        self.log_path = log_path

        logging.config.fileConfig(self.config_path)
        self.logger = logging.getLogger('Kiwoom')
        self.kiwoom_log()
