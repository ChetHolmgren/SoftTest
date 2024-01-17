# -*- coding: utf-8 -*-
# Time:2024/1/11 14:01
# Author:张柘
# File:log.py
# Desc:日志器
from config.config import log_path
import logging

# 创建日志器
logger = logging.getLogger()

# 设置日志器级别
logger.setLevel(logging.INFO)

# 定义处理器参数
format = logging.Formatter('%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')
# 定义处理器
fh = logging.FileHandler(log_path, mode='a', encoding='utf-8')
fh.setLevel(logging.INFO)
fh.setFormatter(format)

# 将处理器添加到日志器中
logger.addHandler(fh)
