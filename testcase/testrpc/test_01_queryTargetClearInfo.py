import pytest
import allure
from operation.eastmoney import queryTargetClearInfo, login_a
#from testcases.conftest import api_data
from common.logger import logger


@allure.step("步骤1 ==>> 登录用户")
def step_1(username):
    logger.info("步骤1 ==>> 登录用户：{}".format(username))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("针对单个接口的测试")
@allure.feature("登录模块")
class TestqueryTargetClearInfo():

    @allure.story("用例--查询优惠券")
    @allure.description("该用例是针对查询目标投清算状态接口的测试")
    @allure.issue("test_01_login.py", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("test_01_login.py", name="点击，跳转到对应用例的链接地址")
    @allure.title("测试数据：id")
    @pytest.mark.single
    def test_queryTargetClearInfo(self, testcase_data):
        logger.info("*************** 开始执行用例 ***************")
        User_id = testcase_data['User_id']
        userinfo = login_a("5407",User_id)
        token = userinfo.response.headers.get("em_tg_session")
        app_sno = testcase_data["app_sno"]
        app_date = testcase_data["app_date"]
        result = queryTargetClearInfo(User_id,token,app_sno,app_date)
        assert result.response.status_code == 200
        b=result.response.headers
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format("0", result.response.json().get("Errcode")))
        assert result.response.json().get("Errcode") == 0
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_01_queryTargetClearInfo.py"])
