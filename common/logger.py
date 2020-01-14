# coding=utf-8

import os
import logging.config

from config.log_config import LOG_DIR, LOGGING_DIC


class Logger(object):

    def __init__(self, logger_name=None):
        """
       1. 如果不传logger_name，则根据__name__去loggers里查找__name__对应的logger配置(__name__为调用文件名)
       获取logger对象通过方法logging.getLogger(__name__)，不同的文件__name__不同，这保证了打印日志时标识信息不同，
       2. 如果传name,则根据name获取loggers对象
       3. 如果拿着name或者__name__去loggers里找key名时却发现找不到，于是默认使用key=''的配置
       """
        self.logger = logging.getLogger(logger_name)
        #  判断日志文件是否存在，不存在则创建
        if not os.path.exists(LOG_DIR):
            os.mkdir(LOG_DIR)

        logging.config.dictConfig(LOGGING_DIC)  # 导入定义的logging配置
        print('self.logger',self.logger)

    def get_logger(self):
        return self.logger

    @staticmethod
    def make_logger(name=None):

        logging.config.dictConfig(LOGGING_DIC)  # 导入定义的logging配置
        if name:
            logger = logging.getLogger(name)
        else:
            logger = logging.getLogger(__name__)
        return logger

# if __name__ == '__main__':
#     log = Logger('default').get_logger()
#     print(log.name)
#     print(log.level)
#     print(log.propagate)