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
to_addr =['1181281178@qq.com', '1114208388@qq.com', '757229511@qq.com', '214155392@qq.com', '857371419@qq.com','1733514239@qq.com',
			'1348861187@qq.com', '979554473@qq.com', '1982764150@qq.com','1378744968@qq.com', '1518570749@qq.com', '1754026982@qq.com',
			'1793015384@qq.com', '3546219@qq.com', '75104172@qq.com', '122712323@qq.com', '137024054@qq.com','736322523@qq.com','205036863@qq.com',
			'272216402@qq.com','277984525@qq.com','286830514@qq.com','306674520@qq.com','314742954@qq.com','344571873@qq.com','347558464@qq.com',
			'354349117@qq.com','398256220@qq.com','419512227@qq.com','423051876@qq.com','438187371@qq.com','452698445@qq.com','470894449@qq.com',
			'490021209@qq.com','497042472@qq.com','543091757@qq.com','543440282@qq.com','565586469@qq.com','583495606@qq.com','597055914@qq.com',
			'599085363@qq.com','599108607@qq.com','634146781@qq.com','643962884@qq.com','498538617@qq.com','674973695@qq.com','709602299@qq.com',
			'742013452@qq.com','772651720@qq.com','786187996@qq.com','787939579@qq.com','837649378@qq.com','844759247@qq.com','851678965@qq.com',
			'876898137@qq.com','979850657@qq.com','1009697209@qq.com','1095583088@qq.com','1216695441@qq.com','1253443812@qq.com','1257004554@qq.com',
			'1347936821@qq.com','1348861187@qq.com','1369392606@qq.com','1437366608@qq.com','1449643995@qq.com','1468769449@qq.com','1481891508@qq.com',
			'1506785369@qq.com','1732621847@qq.com','2669316927@qq.com','2936402771@qq.com']
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
msg.attach(MIMEText('<div style="list-style:none;">' + html  +'<h1 style="text-align:center;">祝你愉快！</h1></div>','html','utf-8'))
server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, to_addr, msg.as_string())
server.quit()

