import os
import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
from email.header import Header
from testcase.conftest import base_data


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEST_CASE_REPORT_PATH = os.path.join(BASE_DIR, 'testcase','my-allure.zip')


class Emailsend():
    def __init__(self):
        self.sender = base_data["init_emain"]["sender"]
        self.receiver = base_data["init_emain"]["receiver"]
        self.smtpserver = base_data["init_emain"]["smtpserver"]
        self.username = base_data["init_emain"]["username"]
        self.password = base_data["init_emain"]["password"]

    def email_content(self):
        with open(TEST_CASE_REPORT_PATH, "rb") as f:
            return f.read()

    # def add_accessory(self, filepath):
    #     res = MIMEText(open(filepath, "rb").read(), "base64", "utf-8")
    #     res.add_header('Content-Disposition', 'attachment', filename=os.path.basename(filepath))
    #     return res

    def send_mail(self):
        f= self.email_content()
        ret= True

        try:
            report_name='报告'
            message = MIMEMultipart()
            mail_title = '主题：测试报告'
            msg = MIMEText('这是接口测试结果……', 'plain', 'utf-8')
            message['From'] = formataddr(["ke1", self.sender])
            message['To'] = formataddr(["ke2", self.receiver])
            message['Subject'] = Header(mail_title, 'utf-8')
            message.attach(msg)  # 邮件正文内容
            t = datetime.strftime(datetime.now(), "%Y%m%d%H%M%S_")
            file_package_path = os.path.join(TEST_CASE_REPORT_PATH, f"{t}{report_name}")
            # 添加附件
            att1 = MIMEText(f, 'html', 'utf-8')
            att1["Content-Type"] = 'application/octet-stream'
            # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
            att1["Content-Disposition"] = 'attachment; filename="report.zip"'
            message.attach(att1)
            # 发送邮件
            server = smtplib.SMTP_SSL(self.smtpserver, 465)
            server.login(self.sender, self.password)  # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(self.sender, [self.receiver, ], message.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭连接
            print('发送成功')
        except smtplib.SMTPException:
            print("发送邮件失败！！！")

if __name__ == '__main__':
    Emailsend().send_mail()



