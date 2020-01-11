import poplib
import email.parser
import email.policy

# 创建与邮件服务器的连接
# conn = poplib.POP3('pop.qq.com',110)#传统的、不安全的
conn = poplib.POP3_SSL('pop.qq.com', 995)  # 基于SSL
conn.set_debuglevel(1)

print(conn.getwelcome().decode('UTF-8'))
# 基本上，POP 3协议的每个命令，就对应此处的一个方法
conn.user('q.qq.com')  # 相当于使用user命令
conn.pass_('passwd')  # 相当于使用pass命令

# 统计邮件信息，相当于stat命令
num, totalsize = conn.stat()
print("邮件数：", num)
print("总大小：", totalsize)

# 获取邮件列表，相当于list命令
resp, maillist, r = conn.list()
print('响应：', resp)
print('邮件列表：', maillist)

# 获取最后一封邮件
resp, maildata, r = conn.retr(len(maillist))
print('响应：', resp)
print('邮件数据：', maildata)
data = b'\r\n'.join(maildata)
# 将邮件数据恢复成EmailMessage对象
msg = email.parser.BytesParser(policy=email.policy.default).parsebytes(data)
# msg代表邮件，应该是EmailMessage对象
print(type(msg))

print('发件人', msg['from'])
print('收件人', msg['to'])
print('主题', msg['subject'])
print('第一个收件人用户名', msg['to'].addresses[0].username)
print('第一个发件人用户名', msg['from'].addresses[0].username)

# 遍历邮件内容，邮件每个部分都是一个part
for part in msg.walk():
    # 'multipart'代表邮件内容的容器，因此无需处理，继续读取它包含的part即可
    if part.get_content_maintype() == 'multipart':
        continue
    # 'multipart'代表邮件的正文
    elif part.get_content_maintype() == 'text':
        print(part.getcontent())
    # 剩下的就是邮件的附件
    else:
        filename = part.get_filename()  # 得到附件的文件名
        # 将附件下载（写入）本地磁盘文件
        with open(filename, 'wb') as f:
            f.write(part.get_payload(decode=True))

# 退出服务器，相当于quit命令
conn.quit()