import logging.config
import datetime

class Logging():
    def __init__(self):
        self.logger = logging.getLogger(__name__)

        format = logging.Formatter("%(asctime)s | %(filename)s | %(lineno)s | %(levelname)s -> %(message)s")

        streamHandler = logging.StreamHandler()
        streamHandler.setFormatter(format)
        self.logger.addHandler(streamHandler)

        d_time = datetime.datetime.now()
        d_str = d_time.strftime("%Y-%m-%d")
        fileHandler = logging.FileHandler("log/"+d_str+".log", encoding="utf-8")
        fileHandler.setFormatter(format)
        self.logger.addHandler(fileHandler)

        self.logger.setLevel(level=logging.DEBUG)