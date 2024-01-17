# -*- coding: utf-8 -*-
# Time:2024/1/4 14:48
# Author:张柘
# File:login_page.py
# Desc:
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LoginPages:
    def __init__(self, driver):
        self.username_page = By.ID, 'account'
        self.password_page = By.NAME, 'password'
        self.click = By.ID, 'submit'
        self.site = By.LINK_TEXT, '地盘'
        self.headshot = By.LINK_TEXT, 'D'
        self.out = By.LINK_TEXT, '退出'
        self.driver = driver

    def input_username(self, username):
        self.driver.find_element(*self.username_page).clear()
        self.driver.find_element(*self.username_page).send_keys(username)

    def input_password(self, password):
        self.driver.find_element(*self.password_page).clear()
        self.driver.find_element(*self.password_page).send_keys(password)

    def login_in(self):
        self.driver.find_element(*self.click).click()

    def logout(self):
        self.driver.switch_to.default_content()
        if WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.site)):
            self.driver.find_element(*self.site).click()
            self.driver.implicitly_wait(10)
            self.driver.switch_to.frame('appIframe-my')
            if WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.headshot)):
                # 登出禅道
                self.driver.find_element(*self.headshot).click()
                self.driver.find_element(*self.out).click()
            else:
                print("页面加载太慢")
        else:
            print('找不到元素')