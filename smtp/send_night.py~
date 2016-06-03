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
to_addr2 =['1181281178@qq.com','498538617@qq.com']
smtp_server = 'smtp.163.com'

msg = MIMEMultipart()
msg['From'] = _format_addr('Jameslong<%s>' % from_addr)
msg['To'] = _format_addr('小鱼<%s>' % to_addr2)
msg['Subject'] = Header('Good night …', 'utf-8').encode()
name = time.localtime()
full_name2 = str(name[0]) + '-' + str(name[1]) + '-' + str(name[2]) + '.mp3'
lrc = "<div style='font-size:24px;color:#a0a0a0;height-light:32px;'>叶子 是不会飞翔的翅膀<br>翅膀 是落在天上的叶子<br>天堂 原来应该不是妄想<br>只是我早已经遗忘<br>当初怎么开始飞翔<br><br>孤单 是一个人的狂欢<br>狂欢 是一群人的孤单<br>爱情 原来的开始是陪伴<br>但我也渐渐地遗忘<br>当时是怎样有人陪伴<br><br>我一个人吃饭 旅行<br>到处走走停停<br>也一个人看书 写信<br>自己对话谈心<br>只是心又飘到了哪里<br>就连自己看也看不清<br>我想我不仅仅是失去你<br><br>我一个人吃饭 旅行<br>到处走走停停<br>也一个人看书 写信<br>自己对话谈心<br>只是心又飘到了哪里<br>就连自己看也看不清<br>我想我不仅仅是失去你<br><br>孤单 是一个人的狂欢<br>狂欢 是一群人的孤单<br>爱情 原来的开始是陪伴<br>但我也渐渐地遗忘<br>当时是怎样有人陪伴<br><br>我一个人吃饭 旅行<br>到处走走停停<br>也一个人看书 写信<br>自己对话谈心<br>只是心又飘到了哪里<br>就连自己看也看不清<br>我想我不仅仅是失去你<br><br>我一个人吃饭 旅行<br>到处走走停停<br>也一个人看书 写信<br>自己对话谈心<br>只是心又飘到了哪里<br>就连自己看也看不清<br>我想我不仅仅是失去你<br><br>叶子 是不会飞翔的翅膀<br>翅膀 是落在天上的叶子<br><br></div>"
msg.attach(MIMEText('<div style="background:url(http://preview.quanjing.com/is026/is09a6j98.jpg );background-size:100% 100%; background-repeat: no-repeat;"><audio src="http://yukunlong.com:8080/music/' + full_name2 +'" controls="controls" autoplay="autoplay"><h1 style="text-align:center;color:#a0a0a0;">小鱼，Good night!</h1>' +lrc+ '<h1 style="text-align:center; font-size:32px;color:#f0f0f0;padding-top:320px;">Good night！</h1></div>','html','utf-8'))


msg_cq = MIMEMultipart()
msg_cq['From'] = _format_addr('小园子<%s>' % from_addr)
msg_cq['To'] = _format_addr('梦园 <%s>' % to_addr)
msg_cq['Subject'] = Header('Good night …', 'utf-8').encode()

full_name =str(name[0]) + '-' + str(name[1]) + '-' + str(name[2]) + '.mp3'

lrc_cq = "<div style='font-size:24px;color:#a0a0a0;height-light:32px;'><br>在我的怀里 在你的眼里<br>那里春风沉醉 那里绿草如茵<br>月光把爱恋 洒满了湖面<br>两个人的篝火 照亮整个夜晚<br>多少年以后 如云般游走<br>那变换的脚步 让我们难牵手<br>这一生一世 有多少你我<br>被吞没在月光如水的夜里<br><br>多想某一天 往日又重现<br>我们流连忘返 在贝加尔湖畔<br><br><br>多少年以后 往事随云走<br>那纷飞的冰雪容不下那温柔<br>这一生一世 这时间太少<br>不够证明融化冰雪的深情<br><br>就在某一天 你忽然出现<br>你清澈又神秘 在贝加尔湖畔<br>你清澈又神秘 像贝加尔湖畔<br><br></div>"
msg_cq.attach(MIMEText('<div style="background:url(http://preview.quanjing.com/is026/is09a6j98.jpg );background-size:100% 100%; background-repeat: no-repeat;"><audio src="http://yukunlong.com:8080/music/' + full_name +'" controls="controls" autoplay="autoplay"><h1 style="text-align:center;color:#a0a0a0;">梦园，Good night!</h1>' +lrc+ '<h1 style="text-align:center; font-size:32px;color:#f0f0f0;padding-top:320px;">Good night！</h1></div>','html','utf-8'))

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr,to_addr2, msg.as_string())
server.sendmail(from_addr,to_addr, msg_cq.as_string())
server.quit()

