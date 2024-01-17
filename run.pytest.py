# -*- coding: utf-8 -*-
# Time:2024/1/10 15:03
# Author:张柘
# File:run.pytest.py
# Desc: 驱动文件
import subprocess

import pytest

pytest.main()
subprocess.call('allure generate ./result/temp -o ./result/report --clean', shell=True)
subprocess.call('allure open -h 127.0.0.1 -p 8883 ./result/report', shell=True)
