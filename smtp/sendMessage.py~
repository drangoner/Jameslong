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


from_addr = '18720977970@163.com'

password = 'yukunlongjiayou1'

to_addr =['1181281178@qq.com','2281582766@qq.com']
smtp_server = 'smtp.163.com'

msg = MIMEMultipart()
msg['From'] = _format_addr('南山一颗树 <%s>' % from_addr)
msg['To'] = _format_addr('Jameslong <%s>' % to_addr)
msg['Subject'] = Header('Best love …', 'utf-8').encode()
#NanChang
url = 'http://www.weather.com.cn/weather/101240101.shtml'
wea = weather.weather(url)
html = wea.getContent()
html = str(html[0])
msg.attach(MIMEText('<div style="background:url(http://d.hiphotos.baidu.com/zhidao/pic/item/c83d70cf3bc79f3d5b4ecce1bba1cd11738b29b7.jpg)"><h1 style="text-align:center;">Jameslong，南昌天气</h1>' + html  +'<h1 style="text-align:center; font-size:32px;color:purple;padding-top:120px;">Good morning！</h1></div>','html','utf-8'))
#ChongQing
url_cq = 'http://www.weather.com.cn/weather/101040100.shtml'
wea_cq = weather.weather(url_cq)
html_cq = wea_cq.getContent()
html_cq = str(html_cq[0])

msg_cq = MIMEMultipart()
msg_cq['From'] = _format_addr('南山一颗树 <%s>' % from_addr)
msg_cq['To'] = _format_addr('梦园 <%s>' % to_addr)
msg_cq['Subject'] = Header('Best love …', 'utf-8').encode()
print(html_cq)
msg_cq.attach(MIMEText('<div style="background:url(http://img4q.duitang.com/uploads/item/201505/31/20150531162433_ukKzf.thumb.224_0.jpeg)"><h1 style="text-align:center;">梦园，重庆天气</h1>' + html_cq +'<h1 style="text-align:center; font-size:32px;color:purple;padding-top:120px;">Good morning！</h1></div>','html','utf-8'))

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr,['1181281178@qq.com'], msg.as_string())
server.sendmail(from_addr, to_addr, msg_cq.as_string())
server.quit()

