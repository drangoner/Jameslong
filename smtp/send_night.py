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
msg['From'] = _format_addr('Jameslong<%s>' % from_addr)
msg['To'] = _format_addr('小鱼 <%s>' % to_addr)
msg['Subject'] = Header('Good night …', 'utf-8').encode()
name = time.localtime()
full_name2 = str(name[0]) + '-' + str(name[1]) + '-' + str(name[2]) + '2.mp3'
lrc = "<div style='font-size:24px;color:#a0a0a0;height-light:32px;'><br>每当我听见忧郁的乐章<br>勾起回忆的伤<br>每当我看见白色的月光<br>想起你的脸庞<br>明知不该去想 不能去想<br>偏又想到迷惘<br>是谁让我心酸 谁让我牵挂<br>是你啊<br>我知道那些不该说的话<br>让你负气流浪<br>想知道多年漂浮的时光<br>是否你也想家<br>如果当时吻你 当时抱你<br>也许结局难讲<br>我那么多遗憾 那么多期盼<br>你知道吗<br>我爱你<br>是多么清楚 多么坚固的信仰<br>我爱你<br>是多么温暖 多么勇敢的力量<br>我不管心多伤 不管爱多慌<br>不管别人怎么想<br>爱是一种信仰<br>把我 带到你的身旁<br>我知道那些不该说的话<br>让你负气流浪<br>想知道多年漂浮的时光<br>是否你也想家<br>如果当时吻你 当时抱你<br>也许结局难讲<br>我那么多遗憾 那么多期盼<br>你知道吗<br>我爱你<br>是多么清楚 多么坚固的信仰<br>我爱你<br>是多么温暖 多么勇敢的力量<br>我不管心多伤 不管爱多慌<br>不管别人怎么想<br>爱是一种信仰<br>把我 带到你的身旁<br>我爱你<br>是忠于自己 忠于爱情的信仰<br>我爱你<br>是来自灵魂 来自生命的力量<br>在遥远的地方<br>你是否一样 听见我的呼喊<br>爱是一种信仰<br>把我 带到你的身旁<br>爱是一种信仰<br>把你 带回我的身旁<br></div>"
msg.attach(MIMEText('<div style="background:url(http://img3.3lian.com/2014/c1/75/d/55.jpg );background-size:100% 100%; background-repeat: no-repeat;"><audio src="http://yukunlong.com:8080/music/' + full_name2 +'" controls="controls" autoplay="autoplay"><h1 style="text-align:center;color:#a0a0a0;">梦园，Good night!</h1>' +lrc+ '<h1 style="text-align:center; font-size:32px;color:#f0f0f0;padding-top:320px;">六一快乐！</h1></div>','html','utf-8'))


msg_cq = MIMEMultipart()
msg_cq['From'] = _format_addr('小园子<%s>' % from_addr)
msg_cq['To'] = _format_addr('梦园 <%s>' % to_addr)
msg_cq['Subject'] = Header('Good night …', 'utf-8').encode()

full_name =str(name[0]) + '-' + str(name[1]) + '-' + str(name[2]) + '.mp3'

lrc_cq = "<div style='font-size:24px;color:#a0a0a0;height-light:32px;'>The snow blows white on the mountain tonight<br>今夜的飘絮席卷了山脉<br>Not a footprint to be seen<br>之前的脚印再无踪影<br>A kingdom of isolation and it looks like I'm the Queen<br>在这个与世隔绝的王国里 我便是至上的王后<br>The wind is howling like the swirling storm inside<br>狂风呼啸 像是要风卷残云<br>Couldn't keep it in, heaven knows I tried<br>再也无法控制 只是天知道我竭尽了全力<br>Don't let them in, don't let them see<br>别让他们进来 别让他们看到<br>Be the good girl<br>只管做好自己<br>You always had to be<br>一如既往地做个好姑娘<br>Conceal, don't feel<br>学会收敛而不是张扬<br>Don't let them know<br>不要让他们知道<br>Well, now they know<br>好吧如今他们也都知道了<br>Let it go<br>就让它去吧<br>Let it go<br>随风而去吧<br>Can't hold it back anymore<br>毋须再继续忍隐屈从<br>Let it go<br>就让它去吧<br>Let it go<br>随风而去吧<br>Turn away and slam the door<br>转身离开 甩门而出<br>I don't care<br>我不会在乎<br>What they're going to say<br>他们的议论<br>Let the storm rage on<br>让风暴来得更猛烈些吧<br>The cold never bothered me anyway<br>我再也不会为寒意所困扰了<br>It's funny how some distance<br>想来有趣的是<br>Makes everything seem small<br>距离让事物变得渺小<br>And the fears that once controlled me<br>而曾经一度控制着我的恐惧<br>Can't get to me at all<br>再也奈何不了我了<br>It's time to see what I can do<br>是时候见识一下我的本领了<br>To test the limits and break through<br>天际再高也要尝试飞翔<br>No right, no wrong, no rules for me<br>没有对错是非，我不会被规则束缚<br>I'm free<br>我已经彻底自由<br>Let it go<br>就让它去吧<br>Let it go<br>随风而去吧<br>I am one with the wind and sky<br>我是乘风飞舞的精灵<br>Let it go<br>就让它去吧<br>Let it go<br>随风而去吧<br>You'll never see me cry<br>你永远不会见到我脆弱而落泪<br>Here I stand<br>我脚下的土地<br>And here I stay<br>将是我的新辟<br>Let the storm rage on<br>让风暴来得更猛烈些吧<br>My power flurries through the air into the ground<br>我的能量在冰天雪地中转换<br>My soul is spiraling in frozen fractals all around<br>我的灵魂在晶莹剔透间盘旋<br>And one thought crystallizes like an icy blast<br>一个念头在漫天雪地中爆破<br>I'm never going back<br>我再也不要回到过去<br>The past is in the past<br>历史已经永远是过去时了<br>Let it go<br>就让它去吧<br>Let it go<br>随风而去吧<br>And I'll rise like the break of dawn<br>我会如破晓的黎明般觉醒<br>Let it go<br>就让它去吧<br>Let it go<br>随风而去吧<br>That perfect girl is gone<br>那个乖乖女已经无处寻觅了<br>Here I stand in the light of day<br>我在此重生 迎着白日的光芒<br>Let the storm rage on<br>让风暴来得更猛烈些吧<br>The cold never bothered me anyway<br>我再也不会为寒意所困扰了<br></div>"
msg_cq.attach(MIMEText('<div style="background:url(http://img-arch.pconline.com.cn/images/bbs4/20091/2/1230832080883.jpg );background-size:100% auto; background-repeat: y-repeat;"><audio src="http://yukunlong.com:8080/music/' + full_name +'" controls="controls" autoplay="autoplay"><h1 style="text-align:center;color:#a0a0a0;">梦园，Good night!</h1>' +lrc_cq+ '<h1 style="text-align:center; font-size:32px;color:#f0f0f0;padding-top:320px;">六一快乐！</h1></div>','html','utf-8'))

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr,['1181281178@qq.com'], msg.as_string())
server.sendmail(from_addr,to_addr, msg_cq.as_string())
server.quit()

