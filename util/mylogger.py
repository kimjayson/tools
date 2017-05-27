#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
该日志类可以把不同级别的日志输出到不同的日志文件中
'''

import os
import sys
import time
import logging
import inspect

handlers = {logging.NOTSET: "/tmp/test_notset.log",
            logging.DEBUG: "/tmp/test_debug.log",
            logging.INFO: "/tmp/test_info.log",
            logging.WARNING: "/tmp/test_warning.log",
            logging.ERROR: "/tmp/test_error.log",
            logging.CRITICAL: "/tmp/test_critical.log"}


def createHandlers():
    for level in handlers.keys():
        path = os.path.abspath(handlers[level])
        handlers[level] = logging.FileHandler(path)


# 加载模块时创建全局变量
createHandlers()


class TNLog(object):
    def printfNow(self):
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    def __init__(self, level=logging.NOTSET):
        self.__loggers = {}
        for level in handlers.keys():
            logger = logging.getLogger(str(level))
            # 如果不指定level，获得的handler似乎是同一个handler?
            logger.addHandler(handlers[level])
            logger.setLevel(level)
            self.__loggers.update({level: logger})

    def getLogMessage(self, level, message):
        frame, filename, lineNo, functionName, code, unknowField = inspect.stack()[2]
        '''日志格式：[时间] [类型] [记录代码] 信息'''
        return "[%s] [%s] [%s - %s - %s] %s" % (
        self.printfNow(), level, filename, lineNo, functionName, message)

    def info(self, message):
        message = self.getLogMessage("info", message)
        self.__loggers[logging.INFO].info(message)

    def error(self, message):
        message = self.getLogMessage("error", message)
        self.__loggers[logging.ERROR].error(message)

    def warning(self, message):
        message = self.getLogMessage("warning", message)
        self.__loggers[logging.WARNING].warning(message)

    def debug(self, message):
        message = self.getLogMessage("debug", message)
        self.__loggers[logging.DEBUG].debug(message)

    def critical(self, message):
        message = self.getLogMessage("critical", message)
        self.__loggers[logging.CRITICAL].critical(message)


if __name__ == "__main__":
    logger = TNLog()
    logger.debug("debug")
    logger.info("info")
    logger.warning("warning")
    logger.error("error")
    logger.critical("critical")