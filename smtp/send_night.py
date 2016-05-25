from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr
import time
import smtplib

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
msg['Subject'] = Header('Good night …', 'utf-8').encode()

msg.attach(MIMEText('<div style="background:url(http://d.hiphotos.baidu.com/zhidao/pic/item/c83d70cf3bc79f3d5b4ecce1bba1cd11738b29b7.jpg)"><h1 style="text-align:center;">Jameslong，Good night!</h1>' +'<p>因为有你，生活变得更加精彩！<br/>感谢你今天的存在！<br/>你的美梦即将到来！</p>'+ '<h1 style="text-align:center; font-size:32px;color:purple;padding-top:120px;">Good night！</h1></div>','html','utf-8'))


msg_cq = MIMEMultipart()
msg_cq['From'] = _format_addr('南山一颗树 <%s>' % from_addr)
msg_cq['To'] = _format_addr('梦园 <%s>' % to_addr)
msg_cq['Subject'] = Header('Good night …', 'utf-8').encode()

msg_cq.attach(MIMEText('<div style="background:url(http://d.hiphotos.baidu.com/zhidao/pic/item/c83d70cf3bc79f3d5b4ecce1bba1cd11738b29b7.jpg)"><h1 style="text-align:center;">梦园，Good night!</h1>' +'<p style="font-size:24px;">宁静的夜晚,<br/>美丽的星空！<br/>你到阳台上看天空，<br/>在你的眼前有两颗流星，<br/>一颗叫晚，<br/>一颗叫安。<br/>划落到你的手中，<br/>你接住了吗？<br/></p>'+ '<h1 style="text-align:center; font-size:32px;color:purple;padding-top:320px;">Good night！</h1></div>','html','utf-8'))

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr,['1181281178@qq.com'], msg.as_string())
server.sendmail(from_addr, to_addr, msg_cq.as_string())
server.quit()

