from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr
import time
import smtplib
import weather
import daily_zhihu

def _format_addr(s):

    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


from_addr = '18720977970@163.com'

password = 'yukunlongjiayou1'

to_addr =['1181281178@qq.com','2281582766@qq.com']
to_addr2 =['1181281178@qq.com','498538617@qq.com']
smtp_server = 'smtp.163.com'

msg = MIMEMultipart()
msg['From'] = _format_addr('Jameslong <%s>' % from_addr)
msg['To'] = _format_addr('小鱼 <%s>' % to_addr2)
msg['Subject'] = Header('I am a robor …', 'utf-8').encode()
#NanChang
url = 'http://www.weather.com.cn/weather/101240101.shtml'
wea = weather.weather(url)
html = wea.getContent()
html = str(html[0])
msg.attach(MIMEText('<div style="background:url(http://img5q.duitang.com/uploads/blog/201410/05/20141005191614_iccht.jpeg);background-size:100% auto; background-repeat: y-repeat;"><h1 style="text-align:center;">Jameslong，南昌天气</h1>' + html  +'<h1 style="text-align:center; font-size:32px;padding-top:120px;">Good morning！</h1></div>','html','utf-8'))
#ChongQing
url_cq = 'http://www.weather.com.cn/weather/101040100.shtml'
wea_cq = weather.weather(url_cq)
html_cq = wea_cq.getContent()
html_cq = str(html_cq[0])

msg_cq = MIMEMultipart()
msg_cq['From'] = _format_addr('南山一颗树 <%s>' % from_addr)
msg_cq['To'] = _format_addr('梦园 <%s>' % to_addr)
msg_cq['Subject'] = Header('I am a robor …', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
msg_cq.attach(MIMEText('<div style="background:url(http://img5q.duitang.com/uploads/blog/201410/05/20141005191614_iccht.jpeg);background-size:100% auto; background-repeat: y-repeat;"><h1 style="text-align:center;">梦园，重庆天气</h1>' + html_cq + '<h1 style="text-align:center; font-size:32px;padding-top:120px;">Good morning！</h1></div>','html', 'utf-8'))
server.sendmail(from_addr,to_addr2, msg.as_string())
server.sendmail(from_addr, to_addr, msg_cq.as_string())

server.quit()

