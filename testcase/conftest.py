import pytest
import os
import allure
from api.user import user
#from common.mysql_operate import db
from common.read_data import data
from common.logger import logger
from core.result_base import ResultBase

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def get_data(yaml_file_name):
    try:
        data_file_path = os.path.join(BASE_PATH, "data", yaml_file_name)
        yaml_data = data.load_yaml(data_file_path)
    except Exception as ex:
        pytest.skip(str(ex))
    else:
        return yaml_data


base_data = get_data("base_data.yml")
api_data = get_data("api_test_data.yml")
scenario_data = get_data("scenario_test_data.yml")


# @allure.step("前置步骤 ==>> 清理数据")
# def step_first():
#     logger.info("******************************")
#     logger.info("前置步骤开始 ==>> 清理数据")
#
#
# @allure.step("后置步骤 ==>> 清理数据")
# def step_last():
#     logger.info("后置步骤开始 ==>> 清理数据")
#
#
# @allure.step("前置步骤 ==>> 管理员用户登录")
# def step_login(username, password):
#     logger.info("前置步骤 ==>> 管理员 {} 登录，返回信息 为：{}".format(username, password))

@pytest.fixture(scope="function")
def logina():
    payload = {
    "Jymm": "321321",
    "Cssj": 1,
    "User_id_lx": "Z",
    "Ex_pwd": "",
    "Czxt": "Czxt",
    "Sblx": "RNandroid",
    "Sjhm": "LIP:NA;MAC:B06EBFBBF70B;IMEI:351564341272474;RMPN:hwCVWJHcbLWBDDjv1C6+xQ==;UMPN:NA;ICCID:NA;OSV:7.1.2;IMSI:460073301724711",
    "Type": "login",
    "Version": "10.1",
    "Yybdm": "5408",
    "User_id": "540860000001",
    "emtoken": "EMRNV1",
    "svrid": "em-secutrade-service",
    "Cssj": "10080",

}
    header = {
        "Content-Type": "application/json;charset=UTF-8",
        "Host": "10.10.84.79:10002"
    }
    result = ResultBase()
    res = user.login(json=payload, headers=header)
    # a=result.json()
    # print(a)
    result.response = res
    logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format("", result.response.json().get("Errcode")))
    # return result
    yield result
#        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format("", result.response.json().get("code")))
#        assert result.response.json().get("code") == 200

# a=logina()
# print("返回值是：%s",a)
# b=a.get("Data")[0].get("Syspm3")
# print(b)
# if __name__ == '__main__':
#     userinfo = logina()
#     #token = userinfo.get("Data").get("Syspm3")
#     print("1111")
#     print(userinfo.json())
#     print("1111")