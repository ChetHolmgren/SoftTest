# -*- coding: utf-8 -*-
# Time:2024/1/9 15:40
# Author:张柘
# File:test_script_4_3_002.py
# Desc:mark的使用
# pytest-ordering插件的使用，需要提前安装，可以自行定义测试用例的执行顺序
# @pytest.mark.run(order=2)来进行排序

# pytest-rerunfailures重新跑一边失败的测试用例，防止因网络波动而出现的偶发情况影响测试结果
#  @pytest.mark.flaky(reruns=3) 易错点：注意是使用reruns而不是rerun,否则只能执行一次

# allure来实现对测试用例的标记和注释，最后体现在allure报告中
import random

import allure
import pytest


# 可以直接对类使用fixture夹具
# @pytest.mark.usefixtures('login')
@allure.feature('登录模块')
class TestCase2:
    # @pytest.mark.flaky(reruns=3)
    # @pytest.mark.run(order=2)
    # @pytest.mark.skipif(2 > 3, reason='跳过')  # 当条件为true的时候跳过，否则不跳，reason中写的是原因
    @allure.story('登录成功的测试用例')
    def test_1(self):
        # r = random.randint(1, 2)
        # assert r == 1
        # # print('打印第四个测试用例')
        with allure.step('输入用户名和密码'):
            print("输入用户名密码")
        with allure.step('点击登录'):
            print('点击登录按钮')

    # @pytest.mark.run(order=1)
    # @pytest.mark.parametrize('username, password',
    #                          [('test001', '123456'), ('test002', '123455')])  # 可以传值，相当于fixture中的params来传递参数
    @allure.story('登录失败的测试用例')
    def test_2(self):
        print('登录失败')


if __name__ == "__main__":
    pytest.main(['-s', '-v', r'selenium\webTest_pytest\test_script_4_3_002.py'])
