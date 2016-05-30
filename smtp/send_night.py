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
name = time.localtime()
full_name =str(name[0]) + '-' + str(name[1]) + '-' + str(name[2]) + '.mp3'
lrc = '<div style="font-size:24px;color:#a0a0a0;height-light:32px;">无数夜睌&nbsp;我们看影碟<br>最爱&nbsp;喜剧&nbsp;内愉快结局<br>无数白昼&nbsp;午饭送恋曲<br>我最懂得知足&nbsp;还有点想哭<br><br>若我病了&nbsp;你递上稀粥<br>揭揭书逐字逐句细读<br>若我极困倦&nbsp;你奉上祝福<br>世界中万大事陪我克服<br>无人像你&nbsp;多么上心<br>给你一百分&nbsp;难得有情人<br>谁明白世间一千亿个可能<br>给我找到一个好人<br>感到极荣幸与相当有运<br>无人像你&nbsp;多么的上心<br>所以别离后&nbsp;周遭也陆沉<br>情人若要走一千亿个可能<br>真相不知怎去追寻<br>一向极愚笨我不懂发问<br><br>极戏剧性&nbsp;快乐却短促<br>美满生活并没有继续<br>或注定结局&nbsp;我没有这福<br>欠你的督促&nbsp;自由太孤独<br>无人像你&nbsp;多么上心<br>给你一百分&nbsp;难得有情人<br>谁明白世间一千亿个可能<br>给我找到一个好人<br>感到极荣幸与相当有运<br>无人像你&nbsp;多么的上心<br><br>所以别离后&nbsp;周遭也陆沉<br>情人若要走一千亿个可能<br>真相不知怎去追寻<br>一向极愚笨我不懂发问<br><br>无人像你&nbsp;多么的上心<br>所以别离后&nbsp;周遭也陆沉<br>情人若要走一千亿个可能<br>真相不知怎去追寻<br>一向极愚笨我不懂发问<br><br></div>'
msg_cq.attach(MIMEText('<div style="background:url(http://img2.3lian.com/2014/f5/73/d/22.jpg );background-size:100% 100%; background-repeat: no-repeat;"><audio src="http://yukunlong.com:8080/music/' + full_name +'" controls="controls" autoplay="autoplay"><h1 style="text-align:center;color:#a0a0a0;">梦园，Good night!</h1>' +lrc+ '<h1 style="text-align:center; font-size:32px;color:#f0f0f0;padding-top:320px;">Good night！</h1></div>','html','utf-8'))

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr,['1181281178@qq.com'], msg.as_string())
server.sendmail(from_addr,to_addr, msg_cq.as_string())
server.quit()

