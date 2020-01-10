import smtplib
import email.message
import email.utils

fromaddr = 'qk@qq.com'
# QQ邮箱要开启安全码
password = 'qqqqqqq'

# 创建SMTP连接
# smtplib.SMTP 代表普通SMTP连接
# smtplib.SMTP_SSL#代表基于SSL的SMTP连接
#conn = smtplib.SMTP('smtp.qq.com', 21)
conn = smtplib.SMTP_SSL('smtp.qq.com', 465)
conn.set_debuglevel(1)
# 登录邮件服务器
conn.login(fromaddr, password)
msg = email.message.EmailMessage()

'''
#设置邮件内容（普通邮件）
msg.set_content('python发送邮件')
'''

'''
# 设置邮件内容（HTML邮件）
msg.set_content('<h2>HTML邮件</h2>'
                + '<div style="border:1px:solid red">html邮件内容</div>', 'html', 'UTF-8')
# 用于设置邮件主题、发件人、收件人
msg['subject'] = 'HTML邮件主题'
msg['from'] = 'qk<%s>' % fromaddr
msg['to'] = 'qkk<%s>' % 'qkk@qq.com'
'''

first_id = email.utils.make_msgid()
# 设置邮件内容（HTML邮件）
msg.set_content('<h2>HTML邮件</h2>'
                + '<div style="border:1px:solid red">html邮件内容</div>'
                + '<img src="cid:' + first_id[1:-1]+'">', 'html', 'UTF-8')
# 用于设置邮件主题、发件人、收件人
msg['subject'] = 'HTML邮件主题'
msg['from'] = 'qk<%s>' % fromaddr
msg['to'] = 'qkk<%s>' % 'qkk@qq.com'

# 添加附件

# 附件指定了cid属性之后，邮件正文就可通过该cid属性值来引用该图片
with open("Chapter/8-5/a.jpg", 'rb') as f:
    msg.add_attachment(f.read(), maintype="image",
                       subtype="jpeg", filename="aaa.jpg", cid=first_id)
with open("Chapter/8-5/b.gif", 'rb') as f:
    msg.add_attachment(f.read(), maintype="image",
                       subtype="gif", filename="bbb.gif")

conn.sendmail(fromaddr, ['qkk@qq.com'], msg.as_string())
# 退出连接
conn.quit()
