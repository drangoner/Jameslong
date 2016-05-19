from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr
import time
import smtplib
import weather

def _format_addr(s):

    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

#from_addr = input('From: ')
from_addr = '18720977970@163.com'
#password = input('Password: ')
password = 'yukunlongjiayou1'
#to_addr = input('To: ')
to_addr =['1181281178@qq.com', '1114208388@qq.com', '757229511@qq.com', '214155392@qq.com', '857371419@qq.com','1733514239',
			'1348861187@qq.com', '979554473@qq.com', '1982764150@qq.com','1378744968@qq.com', '1518570749@qq.com', '1754026982@qq.com',
			'1793015384@qq.com']
#smtp_server = input('SMTP server: ')
smtp_server = 'smtp.163.com'
#msg = MIMEText('<html><body><h1>Hello</h1>'+'<p>send by <a href ="http://www.python.org">Python</a>...</p>'+'</body></html>', 'html', 'utf-8')
msg = MIMEMultipart()
user = '123456789@123.com'
msg['From'] = _format_addr('阿尔曼 <%s>' % from_addr)
msg['To'] = _format_addr('米拉 <%s>' % to_addr)
msg['Subject'] = Header('来自神兽的问候……', 'utf-8').encode()

url = 'http://www.weather.com.cn/weather/101240101.shtml'
wea = weather.weather(url)
html = wea.getContent()
style = 'style="list-style:none;" '
html = str(html[0])
html = html[:4]+style+html[4:]
msg.attach(MIMEText('<div style="list-style:none;">' + html  +'<h1>祝你愉快！</h1></div>','html','utf-8'))
server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, to_addr, msg.as_string())
server.quit()

