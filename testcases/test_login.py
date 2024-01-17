# -*- coding: utf-8 -*-
# Time:2024/1/12 13:06
# Author:张柘
# File:test_login.py
# Desc:
from time import sleep

import allure
import pytest

from data.data import ReadWrite
from objectpage.login_page import LoginPages
from log.log import logger


@allure.feature('登录模块测试')
class TestCase:
    @allure.story('成功登录退出')
    def test_login_out1(self, login):
        self.driver = login
        self.test_login = LoginPages(self.driver)
        data = ReadWrite().excelread('users')
        username = data[0][0]
        password = data[0][1]
        self.test_login.input_username(username)
        self.test_login.input_password(password)
        self.test_login.login_in()
        sleep(0.3)
        assert '地盘 - 禅道' in self.driver.title
        self.test_login.logout()
        logger.info('输入账号密码登录成功')

    # @allure.story('输入用户名不输入密码')
    # def test_login_out2(self, login):
    #     with allure.step('输入用户名不输入密码'):
    #         self.driver = login
    #         test_login = LoginPages(self.driver)
    #         data = ReadWrite().excelread('users')
    #         test_login.input_username(data[0])
    #     with allure.step('点击登录按钮'):
    #         test_login.click()
    #     with allure.step('点击弹出框的同意按钮'):
    #         self.driver.switch_to.alert.accept()
