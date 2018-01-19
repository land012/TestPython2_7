#! /usr/bin/env python
# -*- coding: utf8
import os
import smtplib,email,email.MIMEBase,email.MIMEText
import sys
from email import Utils
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
path = os.getcwd()


#python方式 邮件发送
def send_w(subject, message, temail):
    msg = email.MIMEText.MIMEText(message, _subtype='html', _charset='utf-8')
    femail = 'opviss@163.com'
    msg['To'] = ', '.join(temail)
    msg['From'] = femail
    msg['Subject'] = subject
    msg['Date'] = Utils.formatdate(localtime=1)
    print msg.as_string()
    s = smtplib.SMTP()
    s.connect('smtp.163.com')
    s.login('opviss', '432165')
    s.sendmail(femail, temail, msg.as_string())
    s.close()


def send_w_att(subject, message, temail,attfileList):
    txt=MIMEText(unicode(message),'plain','utf-8')
    msg = MIMEMultipart()
    msg.attach(txt)
    femail = 'wathclog@baidu.com'
    if attfileList is not None:
     for attfile in attfileList:
        file=open(attfile["path"], 'rb')
        att = MIMEText(file.read(), 'base64', 'utf8')
        file.close()
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename="'+attfile["name"]+'"'
        msg.attach(att)
    msg['To']=temail
    msg['From'] = femail
    msg['Subject'] = subject
    msg['Date'] = Utils.formatdate(localtime=1)
    print msg.as_string()
    s = smtplib.SMTP('mail2-in.baidu.com')
    s.sendmail(femail,temail.split(";"), msg.as_string())
    s.close()


def send_w_html(subject, message, temail):
    txt=MIMEText(unicode(message),'html',"utf-8")
    msg = MIMEMultipart("alternative")
    msg.attach(txt)
    femail = 'wathclog@baidu.com'
    msg['To']=temail
    msg['From'] = femail
    msg['Subject'] = subject
    msg['Date'] = Utils.formatdate(localtime=1)
    print msg.as_string()
    s = smtplib.SMTP('mail2-in.baidu.com')
    s.sendmail(femail,temail.split(";"), msg.as_string())
    s.close()


#shell 方式邮件发送
def send_l(subject,message,temail):
    f = open(path+"/tmp.txt","w")
    f.write('To:'+temail)
    f.write(os.linesep)
    f.write('From:watchlog@baidu.com')
    f.write(os.linesep)
    f.write('Subject:'+subject)
    f.write(os.linesep)
    f.write("Content-type:text/html;charset='gbk'")
    f.write(os.linesep)
    f.write(message)
    f.write(os.linesep)
    f.close()
    os.system('iconv -f utf-8 -t gbk tmp.txt > tmp_gbk.txt')
    os.system('/usr/lib/sendmail -t <tmp_gbk.txt 2> /dev/null')
    os.remove(path+"/tmp.txt")
    os.remove(path+'/tmp_gbk.txt')


def send_ll(subject,message,temail):
    f = open(path+"/tmp.txt","w")
    f.write('To:'+temail)
    f.write(os.linesep)
    f.write('From:watchlog@baidu.com')
    f.write(os.linesep)
    f.write('Subject:'+subject)
    f.write(os.linesep)
    f.write("Content-type:text/html;charset='gbk'")
    f.write(os.linesep)
    f.write(message)
    f.write(os.linesep)
    f.close()
    os.system('iconv -f utf-8 -t gbk tmp.txt > tmp_gbk.txt')


def sendMail(data,history,history_file,login_title,title,temail):
    content=''
    if(history == 1):
        f = file(history_file,"r")
        content = f.read()
        f.close()

        f = file(history_file,"w")
        f.write(data)
        f.write(os.linesep)
        f.write(content)
        f.close()

    message = "<style> *{ font-size:12pt;font-weight:700 } td{border: 1px solid #000}</style>"
    message += "<table style='border-collapse:collapse; font-size:9pt'><caption>"+title+"</caption>"
    message += login_title
    message+= data
    message += content
    message += "</table>"
    #temail = ["liuhaibin@baidu.com"]
    #temail = "lxb-rd@baidu.com luowenwen01@baidu.com fanqin@baidu.com fanchunxia@baidu.com chengfang01@baidu.com sunxianqun@baidu.com liuhongshu@baidu.com"
    #temail = 'liuhaibin@baidu.com'
    send_l(title,message, temail)

