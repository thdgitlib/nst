import pytest
import allure
from operation.eastmoney import modifyplan
from operation.eastmoney import queryFinanceCoupons
from testcase.conftest import api_data
from common.logger import logger
from operation.eastmoney import login_a




@allure.step("步骤1 ==>> 登录用户")
def step_1(username):
    logger.info("步骤1 ==>> 登录用户：{}".format(username))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("针对单个接口的测试")
@allure.feature("定投")
class TestModifyplan():

    @allure.story("用例--修改定投")
    @allure.description("该用例是针对修改定投接口的测试")
    @allure.issue("https://www.baidu.com", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.baidu.com", name="点击，跳转到对应用例的链接地址")
    @allure.title("测试数据：id")
    # @pytest.mark.parametrize("id,queryType,except_result,except_code,except_msg",api_data["test_queryFinanceCoupons"])
    def test_modifyplan(self):
        id = '540700000012'
        operType = '1'
        step_1("用户1")
        stopYield= 0.03
        userinfo = login_a("5407",id)
        token = userinfo.response.headers.get("em_tg_session")
        print(token)
        logger.info("*************** 开始执行用例 ***************")
        with allure.step("步骤2"):
            result = modifyplan(id,operType,stopYield,token)
        assert result.response.status_code == 200
        print(result.response.text)
        #        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format("", result.response.json().get("code")))
        #        assert result.response.json().get("code") == 200
        logger.info("*************** 结束执行用例 ***************")
#    @pytest.mark.usefixtures
#     def test_query(self,logina, id="540860000001"):
#         userinfo=logina
#         print(userinfo)
#         token=userinfo.headers.get("em_tg_session")
#         logger.info("*************** 开始执行用例 ***************")
#         result = queryFinanceCoupons(id,token)
#         assert result.response.status_code == 200
#         print("66666666666666")
#         print(result.response.status_code)
#         print(result.response.text)
#         print("777777777777777777")
# #        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format("", result.response.json().get("code")))
# #        assert result.response.json().get("code") == 200
#         logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_modifyplan.py"])
