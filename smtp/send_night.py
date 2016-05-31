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
msg['From'] = _format_addr('小园子<%s>' % from_addr)
msg['To'] = _format_addr('Jameslong <%s>' % to_addr)
msg['Subject'] = Header('Good night …', 'utf-8').encode()

msg.attach(MIMEText('<div style="background:url(http://d.hiphotos.baidu.com/zhidao/pic/item/c83d70cf3bc79f3d5b4ecce1bba1cd11738b29b7.jpg)"><h1 style="text-align:center;">Jameslong，Good night!</h1>' +'<p>因为有你，生活变得更加精彩！<br/>感谢你今天的存在！<br/>你的美梦即将到来！</p>'+ '<h1 style="text-align:center; font-size:32px;color:purple;padding-top:120px;">Good night！</h1></div>','html','utf-8'))


msg_cq = MIMEMultipart()
msg_cq['From'] = _format_addr('小园子<%s>' % from_addr)
msg_cq['To'] = _format_addr('梦园 <%s>' % to_addr)
msg_cq['Subject'] = Header('Good night …', 'utf-8').encode()
name = time.localtime()
full_name =str(name[0]) + '-' + str(name[1]) + '-' + str(name[2]) + '.mp3'

lrc = "<div style='font-size:24px;color:#a0a0a0;height-light:32px;'><br>I know so many places in the world<br>世界是如此之大<br>I follow the sun in my silver plane<br>在银白色飞机上追随着阳光<br>Universal traveler<br>去做个环球旅行者吧<br>Universal traveler<br>环游世界的旅行者<br>Universal traveler<br>环游世界的旅行者<br>Universal traveler<br>环游世界的旅行者<br>If you have a look<br>如果你也期待<br>Outside on the sea<br>深海外<br>Everything is white<br>所有的纯白<br>It's so wonderful<br>那是多美妙的天堂<br>Universal traveler<br>去做个环球旅行者吧<br>Universal traveler<br>环游世界的旅行者<br>Universal traveler<br>环游世界的旅行者<br>Universal traveler<br>环游世界的旅行者<br><br>So far  so far<br>一直一直<br>So far away<br>那么远<br><br>I met so many<br>我曾遇到过许多<br>People in my life<br>生命中的路人<br>I've got many friends<br>我也曾得到许多<br>Who can care for me<br>在乎我的朋友<br>Universal traveler<br>去做个环球旅行者吧<br>Universal traveler<br>环游世界的旅行者<br>Universal traveler<br>环游世界的旅行者<br>Universal traveler<br>环游世界的旅行者<br><br>Just feel everywhere at home<br>家的感觉无处不在<br>Tomorrow<br>当旭日再次东升<br>Is a brand new day<br>又标识了新的一天<br>Let us go somewhere else<br>勇敢去闯荡世界吧<br>Universal Traveler<br>做个环球旅行者<br>Universal traveler<br>环游世界的旅行者<br>Universal traveler<br>环游世界的旅行者<br>Universal traveler<br>环游世界的旅行者<br><br>So far  so far<br>一直一直<br>So far away<br>那么远<br></div>"
msg_cq.attach(MIMEText('<div style="background:url(http://img2.3lian.com/2014/f5/73/d/22.jpg );background-size:100% 100%; background-repeat: no-repeat;"><audio src="http://yukunlong.com:8080/music/' + full_name +'" controls="controls" autoplay="autoplay"><h1 style="text-align:center;color:#a0a0a0;">梦园，Good night!</h1>' +lrc+ '<h1 style="text-align:center; font-size:32px;color:#f0f0f0;padding-top:320px;">Good night！</h1></div>','html','utf-8'))

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr,['1181281178@qq.com'], msg.as_string())
server.sendmail(from_addr,['1181281178@qq.com'], msg_cq.as_string())
server.quit()

