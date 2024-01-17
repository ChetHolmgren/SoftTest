# -*- coding: utf-8 -*-
# Time:2024/1/9 15:38
# Author:张柘
# File:conftest.py
# Desc:
from config.config import driver_path, zan_dao_url
import pytest
from selenium.webdriver.edge.service import Service
from selenium import webdriver


# params传值
@pytest.fixture(scope='session')  # fixture()函数，可以作为参数进行传递；可以设置夹具的作用范围scope='function','class','module','session'
def login():
    e = Service(executable_path=driver_path)  # 驱动路径
    driver = webdriver.Edge(service=e)  # 加载驱动
    driver.maximize_window()  # 打开浏览器窗口
    driver.get(zan_dao_url)  # 进入禅道登录页面
    yield driver  # 等待测试步骤进行
    driver.quit()  # 退出浏览器
