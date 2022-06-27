from core.result_base import ResultBase
from api.user import user,backup
from common.logger import logger
import time

# def queryFinanceCoupons1():
#     """
#     获取全部优惠券信息
#     :return: 自定义的关键字返回结果 result
#     """
#     result = ResultBase()
#     res = user.queryCoupons()
#     result.success = False
#     if res.json()["code"] == 0:
#         result.success = True
#     else:
#         result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["msg"])
#     result.msg = res.json()["msg"]
#     result.response = res
#     return result
def login_a(Yybdm, User_id):
    """
    登录用户
    :param username: 用户名
    :param password: 密码
    :return: 自定义的关键字返回结果 result
    """
    payload = {
        "Jymm": "321321",
		"Cssj":1,
		"User_id_lx":"Z",
		"Ex_pwd":"",
		"Czxt": "Czxt",
		"Sblx": "RNandroid",
		"Sjhm": "LIP:NA;MAC:B06EBFBBF70B;IMEI:351564341272474;RMPN:hwCVWJHcbLWBDDjv1C6+xQ==;UMPN:NA;ICCID:NA;OSV:7.1.2;IMSI:460073301724711",
		"Type": "login",
		"Version": "10.1",
		"Yybdm": Yybdm,
		"User_id": User_id,
        "emtoken": "EMRNV1",
        "Cssj": "10080",
        "svrid": "em-secutrade-service"

    }
    header = {
        "Content-Type": "application/json;charset=UTF-8",
        "User-Agent":"Fiddler",
        "Host": "10.10.81.228:8081",
        "Content-Length": "400"
    }
    result = ResultBase()
    res = user.login(json=payload, headers=header)
    result.success = False
    if res.json()["Status"] == 0:
        result.success = True
#        result.token = res.json()["login_info"]["token"]
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["Status"], res.json()["Message"])
#    result.msg = res.json()["Message"]
    result.response = res
    logger.info("登录用户 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result

def queryFinanceCoupons(User_id="",queryType='',token=""):
    """
    获取全部优惠券信息
    :return: 自定义的关键字返回结果 result
    """
    t=time.time()
    ts = int(round(t*1000))
    result = ResultBase()
    json_data = {
	"Czxt": "Czxt",
	"Sblx": "RNandroid",
	"Sjhm": "LIP:NA;MAC:B06EBFBBF70B;IMEI:351564341272474;RMPN:hwCVWJHcbLWBDDjv1C6+xQ==;UMPN:NA;ICCID:NA;OSV:7.1.2;IMSI:460073301724711",
	"Type": "queryFinanceCoupons",
	"Version": "10.1",
	"Yybdm": "5408",
	"User_id_lx": "Z",
	"User_id": User_id,
	"emtoken": "EMRNV1",
	"svrid": "em-secutrade-service",
	"queryType": queryType,
	"Zczh": User_id,
	"Syspm3": token,
	"custCode": User_id,
	"cust_code": User_id,
	"CUST_CODE": User_id,
	"CUST_ID": User_id,
	"custId": User_id,
	"Khdm": User_id,
	"USER_TYPE": "0",
	"gw_reqtimestamp": ts
}

    header = {
        "Content-Type": "application/json;charset=utf-8",
        "em_tg_session":token
    }
    res = user.queryCoupons(json=json_data, headers=header)
    result.success = False
    if res.json()["Status"] == 0:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["Status"], res.json()["Message"])
        result.msg = res.json()["Message"]
    result.response = res
    logger.info("查询信息 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result

def modifyplan(User_id="",operType='',stopYield='',token=""):
    """
    获取全部优惠券信息
    :return: 自定义的关键字返回结果 result
    """
    t=time.time()
    ts = int(round(t*1000))
    result = ResultBase()
    json_data = {
            "Czxt": "android_101",
            "Sblx": "RNandroid",
            "Sjhm": "LIP:NA;MAC:B06EBFBBF70B;IMEI:351564341272474;RMPN:hwCVWJHcbLWBDDjv1C6+xQ==;UMPN:NA;ICCID:NA;OSV:7.1.2;IMSI:460073301724711",
            "Type": "modifyPlan",
            "Version": "10.1",
            "Yybdm": "5407",
            "User_id_lx": "Z",
            "User_id": User_id,
            "emtoken": "EMRNV1",
            "svrid": "em-secutrade-service",
            "appsNo": "0000097604",
            "appDate": "20220505",
            "bgnDate": "20220506",
            "instCode": "007666",
            "ordAmt": "100",
            "transAcct": "68200540700000012",
            "paidCycle": "2",
            "cycleSendDay": "0",
            "operType": operType,
            "investType": "0",
            "isTargetInvest": "1",
            "stopYield": stopYield,
            "stopStrategy": "0",
            "Zczh": User_id,
            "Syspm3": token,
            "custCode": User_id,
            "cust_code": User_id,
            "CUST_CODE": User_id,
            "CUST_ID": User_id,
            "custId": User_id,
            "Khdm": User_id,
            "USER_TYPE": "0",
            "gw_reqtimestamp": ts
        }


    header = {
        "Content-Type": "application/json;charset=utf-8",
        "em_tg_session":token
    }
    res = user.modifyplan(json=json_data, headers=header)
    result.success = False
    if res.json()["Status"] == 0:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["Status"], res.json()["Message"])
        result.msg = res.json()["Message"]
    result.response = res
    logger.info("查询信息 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def queryTargetClearInfo(User_id="",token="",app_sno='',app_date=''):
    """
    获取全部优惠券信息
    :return: 自定义的关键字返回结果 result
    """
    t=time.time()
    ts = int(round(t*1000))
    result = ResultBase()
    json_data = {
	"Czxt": "Czxt",
	"Sblx": "RNandroid",
	"Sjhm": "LIP:NA;MAC:B06EBFBBF70B;IMEI:351564341272474;RMPN:hwCVWJHcbLWBDDjv1C6+xQ==;UMPN:NA;ICCID:NA;OSV:7.1.2;IMSI:460073301724711",
	"Type": "queryTargetClearInfo",
	"Version": "10.1",
	"Yybdm": "5407",
	"User_id_lx": "Z",
	"User_id": User_id,
	"emtoken": "EMRNV1",
	"svrid": "em-secutrade-service",
	"Zczh": User_id,
	"Syspm3": token,
	"custCode": User_id,
	"cust_code": User_id,
	"CUST_CODE": User_id,
	"CUST_ID": User_id,
	"custId": User_id,
	"Khdm": User_id,
	"USER_TYPE": "0",
    "app_sno":app_sno,
    "app_date":app_date,
	"gw_reqtimestamp": ts
}

    header = {
        "Content-Type": "application/json;charset=utf-8",
        "em_tg_session":token
    }
    res = backup.queryTargetClearInfo(json=json_data, headers=header)
    result.success = False
    if res.json()["Status"] == 0:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["Status"], res.json()["Message"])
        result.msg = res.json()["Message"]
    result.response = res
    logger.info("查询信息 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result
# if __name__ == '__main__':
#     userinfo=login_a("5407",'540700000012').json()
#     #token = userinfo.headers.get("em_tg_session")
#     print(userinfo)