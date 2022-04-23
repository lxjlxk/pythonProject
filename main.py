
import smtplib

from email.mime.text import MIMEText

from email.header import Header



from_addr = '1730550266@qq.com'
password = '1928374655lxk.'

to_addr = '513841979@qq.com'

smtp_server = 'smtp.qq.com'


msg = MIMEText('test', 'plain', 'utf-8')

msg['From'] = Header('zhangsan')
msg['To'] = Header('lisi')
subject = 'Python SMTP test'
msg['Subject'] = Header(subject, 'utf-8')

try:
    smtpobj = smtplib.SMTP_SSL(smtp_server)

    smtpobj.connect(smtp_server, 465)

    smtpobj.login(from_addr, password)

    smtpobj.sendmail(from_addr, to_addr, msg.as_string())
    print("success")
except smtplib.SMTPException:
    print("fail")
finally:

    smtpobj.quit()

