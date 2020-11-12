#处理器三大模块
# 日志器  日志的入口  比喻为：日记本（日志级别：info（信息级别） debug warning error critical(致命错误)）
# 格式器  以什么样的格式处理
# 处理器  日志输入方式等
import logging.handlers
import os
file_path=os.path.dirname(os.path.dirname(__file__))+"/logger/test.log"
class GegLogger:
    logger=None
    @classmethod
    def get_logger(cls):
        if cls.logger==None:
            # 获取日志器
            cls.logger=logging.getLogger()
            cls.logger.setLevel(logging.INFO)
            # 设置日志的显示格式
            fmt="%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
            # 获取格式器
            fm=logging.Formatter(fmt)
            # 获取处理器
            tf=logging.handlers.TimedRotatingFileHandler(filename=file_path,when="h",interval=1,backupCount=3,encoding="utf-8")
            # 在处理器中添加格式器
            tf.setFormatter(fm)
            tf.setLevel(logging.INFO)
            cls.logger.addHandler(tf)
        return cls.logger
if __name__ == '__main__':
    logger=GegLogger.get_logger()
    logger.info("testinfo1")
    logger.debug("testdebug1")
    logger.error("testerror1")
    logger.warn("testwarn1")
    logger.critical("testcritical1")

