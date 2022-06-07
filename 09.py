import multiprocessing
def get_cpu_info():
    cpu_count = multiprocessing.cpu_count()
    print(cpu_count) ##  cat /proc/cpuinfo| grep "processor"| wc -l
    return str(cpu_count)

import psutil
def get_ps():
    
    mem = psutil.virtual_memory()

    total = float(mem.total) / 1024 / 1024 / 1024
    used = float(mem.used) / 1024 / 1024 / 1024
    free = float(mem.free) / 1024 / 1024 / 1024

    return total,used,free

import socket
def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('119.29.29.29', 80))
        ip = s.getsockname()[0]
    except:
        print("network error")
    finally:
        s.close()    
    return ip

print(get_ps())
print(get_host_ip())

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender = 'w0x7ce@qq.com' 
passwd = 'caipvyjxknptbgeh'   

to= ['w0x7ce@qq.com'] #接受方邮箱

msg = MIMEMultipart()

try:
    content = "CPU count %s \n" % get_cpu_info()
    content +="Memory information  total %s used %s free %s \n" % get_ps() 
    content += "Server IP %s \n" % get_host_ip
except :
    print("format error")

msg.attach(MIMEText(content,'plain','utf-8'))
msg['Subject']="Server_information"
msg['From']= sender

try:
    s = smtplib.SMTP_SSL("smtp.qq.com", 465)
    s.login(sender, passwd)
    s.sendmail(sender,to,msg.as_string())
    print("邮件发送成功")
except :
    print("Network error")
