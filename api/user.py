import os
from core.rest_client import RestClient
from common.read_data import data

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
api_root_url = data.load_ini(data_file_path)["host"]["api_root_url"]
backup_url = data.load_ini(data_file_path)["host"]["backup_url"]

class User(RestClient):

    def __init__(self, api_root_url, **kwargs):
        super(User, self).__init__(api_root_url, **kwargs)

    def login(self, **kwargs):
        return self.post("/api/Customer/login", **kwargs)

    def queryCoupons(self, **kwargs):
        return self.post("/api/OTC/queryFinanceCoupons", **kwargs)

    def modifyplan(self, **kwargs):
        return self.post("/api/Fund/modifyPlan", **kwargs)

user = User(api_root_url)


class Backup(RestClient):
    def __init__(self,backup_url, **kwargs):
        super(Backup, self).__init__(backup_url, **kwargs)

    def queryTargetClearInfo(self, **kwargs):
        return self.post("/api/Fund/queryTargetClearInfo", **kwargs)

backup = Backup(backup_url)
