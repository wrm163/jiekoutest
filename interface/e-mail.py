import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

import os, sys
from nt import chdir             #判断目录是否存在并切换目录

print("正在发送...")
#登陆邮件服务器
smtpObj=smtplib.SMTP('smtp.qq.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
#传入相应的账号/密码信息
smtpObj.login('1412182594@qq.com', 'dfsdagfiabobjjff')

#邮件收发信人信息
sender = '1412182594@qq.com'#发件人信息
receivers = ['1412182594@qq.com']#收件人信息

#完善发件人收件人，主题信息
message = MIMEMultipart()
message['From'] = formataddr(["王瑞敏", sender])
message['To'] = formataddr(["ls", '1412182594.com'.join(receivers)])
subject = '(标题)'
message['Subject'] = Header(subject, 'utf-8')

#正文部分
textmessage = MIMEText('(输入的内容)', 'html', 'utf-8')
message.attach(textmessage)

workLoc = os.path.join('D:\\','python','Python daima','interface')
# #检查路径有效性
if (os.path.exists(workLoc)) & (os.path.isdir(workLoc)):
#尝试改变当前工作路径：
    chdir(workLoc)
else:
    print('路径无效，请从新检查')
    sys.exit()

#尝试添加附件（File 里面可以随意更换任何图片、文件）
File = '讲师评价系统.html'
print("附件文件名为：%s" %File)
FileLoc = os.path.join(workLoc, File)
FileAtt = MIMEApplication(open(FileLoc, 'rb').read())
FileAtt.add_header('Content-Disposition', 'attachment', filename=File)
message.attach(FileAtt)

#发送邮件操作
smtpObj.sendmail(sender, receivers, message.as_string())
smtpObj.quit()
print("发送成功！")


# import smtplib
# import email.utils
# from email.mime.text import MIMEText
#
# class Msg():
#      def __init__(self):
#          pass
#
#      @staticmethod
#      def creat_msg():
#          # Creat mail information
#          msg = MIMEText('Come on', 'plain', 'utf-8')
#          msg['From'] = email.utils.formataddr(('Author', '1412182594@qq.com'))
#          msg['To'] = email.utils.formataddr(('Recipient', '1981288305@qq.com'))
#          msg['Subject'] = email.utils.formataddr(('Subject', 'Good good study, day day up!'))
#
#          return msg
#
# class EmailServer():
#      def __init__(self):
#          pass
#
#      @staticmethod
#      def config_server():
#          # Configure mailbox
#          config = dict()
#          config['send_email']= '1412182594@qq.com'
#          config['passwd'] = 'wangruimin123'
#          config['smtp_server'] = 'smtp.qq.com'
#          config['target_email'] = '1981288305@qq.com'
#          return config
#
#      def send_email(self):
#          # Use smtp to send email to the target mailbox
#          msg = Msg.creat_msg()
#          config = self.config_server()
#
#          server = smtplib.SMTP()
#          server.connect(host=config['smtp_server'], port=25)
#          server.login(user=config['send_email'], password=config['passwd'])
#          server.set_debuglevel(True)
#
#          try:
#              server.sendmail(config['send_email'],
#                              [config['target_email']],
#                              msg.as_string())
#          finally:
#              server.quit()
#
# if __name__ == '__main__':
#     emailServer = EmailServer()
