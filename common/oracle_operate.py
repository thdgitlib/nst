import cx_Oracle as cx
import os
from common.read_data import data
from common.logger import logger

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
data1 = data.load_ini(data_file_path)["oracle2"]

OC_CONF = {
    "user": data1["ORACLE_USER"],
    "password": data1["ORACLE_PASSWD"],
    "dsn": data1["ORACLE_HOST"]
}

# sql="select * from run.EM_DB_ROUTE"
# sql1="select * from run.em_sdx_holdsign WHERE ZJZH = 54150000010 ORDER BY EUTIME DESC"
# oc = cx.connect(user=OC_CONF["user"],password=OC_CONF["password"],dsn=OC_CONF["dsn"])
# cur = oc.cursor()
# cur.execute(sql)
# for row in cur:
#     print(row)
# oc.close()
class OcDb():

    def __init__(self, db_conf=OC_CONF):
        # 通过字典拆包传递配置信息，建立数据库连接
        self.conn = cx.connect(user=OC_CONF["user"],password=OC_CONF["password"],dsn=OC_CONF["dsn"])
        # 通过 cursor() 创建游标对象
        self.cur = self.conn.cursor()

    def __del__(self):  # 对象资源被释放时触发，在对象即将被删除时的最后操作
        # 关闭游标
        self.cur.close()
        # 关闭数据库连接
        self.conn.close()

    def select_db(self, sql):
        """查询"""
        # 检查连接是否断开，如果断开就进行重连
        self.conn.ping()
        # 使用 execute() 执行sql
        self.cur.execute(sql)
        # 使用 fetchall() 获取查询结果
        data = self.cur.fetchall()
        column_names = list(map(lambda x: x.lower(), [d[0] for d in self.cur.description]))
        # list of data items
        rows = list(data)
        result = [dict(zip(column_names, row)) for row in rows]
        return result
        # for i in data:
        #     list1 = list(i)
        #     des = self.cur.description
        #     # print("表的描述:", des)
        #     t = ",".join([item[0] for item in des])
        #     print(type(t))
        #     watch_head = t.split(',')
        #     print(watch_head)
        #     dict1 = dict(zip(watch_head, list1))
        # return dict1

    def execute_db(self, sql):
        """更新/新增/删除"""
        try:
            # 检查连接是否断开，如果断开就进行重连
            self.conn.ping(reconnect=True)
            # 使用 execute() 执行sql
            self.cur.execute(sql)
            # 提交事务
            self.conn.commit()
        except Exception as e:
            logger.info("操作MySQL出现错误，错误原因：{}".format(e))
            # 回滚所有更改
            self.conn.rollback()


OC = OcDb(OC_CONF)

