import os, sys

# 获取当前文件的绝对路径
current_path = os.path.abspath(__file__)
# 获取当前文件的父目录
parent_path = os.path.dirname(current_path)
# 将父目录添加到 sys.path 中
sys.path.append(parent_path)

from config.packages import *

logdir = ""

class Logger:
    def __init__(self, log_file='app.log', log_level=logging.INFO,
                 log_format='%(asctime)s - %(levelname)s - %(message)s'):
        # 创建一个logger对象
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)

        # 创建一个文件处理器
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(log_level)

        # 创建一个控制台处理器
        console_handler = logging.StreamHandler()
        console_handler.setLevel(log_level)

        # 创建一个格式化器并将其添加到处理器
        formatter = logging.Formatter(log_format)
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # 将处理器添加到logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)
