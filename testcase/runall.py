# !/usr/bin/env python
# _*_coding:utf-8_*_
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.abspath(os.path.dirname(curPath) + os.path.sep + ".")
sys.path.append(rootPath)
# 上述引用是为了解决jenkins报错

import pytest, os, allure
import zipfile
# from common.sendemail import Emailsend

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEST_CASE_REPORT_PATH = os.path.join(BASE_DIR, 'testcase','report1')

if __name__ == "__main__":
    pytest.main(['-s', ''])
    # 生成测试报告json
    # pytest.main(["-s", "-q", '--alluredir', 'F:/pythonspace/eastmoney/testcase/report'])
    # # 将测试报告转为html格式
    split = 'allure ' + 'generate ' + './temp ' + '-o ' + './report1/report ' + '--clean'
    # os.system('cd C:/Users/lili/PycharmProjects/PytestAutomation/report')
    os.system(split)
    # print(split)
    # # 发送邮件
    # z = zipfile.ZipFile('my-allure.zip', 'w', zipfile.ZIP_DEFLATED)
    # startdir = TEST_CASE_REPORT_PATH
    # for dirpath, dirnames, filenames in os.walk(startdir):
    #     for filename in filenames:
    #         z.write(os.path.join(dirpath, filename))
    # z.close()
    # s=Emailsend()
    # s.send_mail()


    # pytest --alluredir F:/pythonspace/eastmoney/testcase/report F:/pythonspace/eastmoney/testcase/runall.py --clean-alluredir
