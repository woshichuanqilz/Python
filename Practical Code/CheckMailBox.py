#coding=UTF-8
import poplib
import re
import string
import time
from subprocess import Popen
from subprocess import PIPE
import win32api
import win32con
####第一部分：收取邮件，获取最新一封的标题，使用poplib模块####
host='pop3.163.com'  #这里以163邮箱举例
username='m15831016489_1@163.com'
password='woshichuanqilz72'   #可以用您的小号
while True:
         
        pp=poplib.POP3(host)          ##连接163邮件服务器
 
        #pp.set_debuglevel(1)         ##debug
        pp.user(username)
        pp.pass_(password)            ##发送用户名密码校验
 
        res_t=r"Subject:([^']*)"
        p_tel_t=re.compile(res_t)         ##正则表达式，匹配标题内容
        #res_r=r'From:.*<(.*)>'
        #p_tel_r=re.compile(res_r)       ##正则表达式，匹配发件邮箱地址
 
        ret=pp.stat()
        num=ret[0]                    ##统计总共有多少封邮件
 
        down=str(pp.retr(num))        ##提取第num封邮件的信息,也就是最新一封
 
        p_list_t=p_tel_t.findall(down)      
        #p_list_r=p_tel_r.findall(down)
        title=string.strip(p_list_t[0]) ##抓取第一封邮件信息内的标题内容
        pp.quit()                     ##关闭连接
        #print p_list_r[0]
 
        ####第二部分：将邮箱内邮件的数量写入txt，下次运行时只需读取txt数值与当前比较，一样则不运行###
        files=open('./num.txt','r')
        num_txt=files.read()
        files.close()
 
        if str(num_txt)==str(num):
            pass
        else:
            files=open('./num.txt','w')
            files.write(str(num))
            files.close()
        ####第三部分:python执行CMD命令,使用Popen模块####
            win32api.MessageBox(0,u'远程下达的指令: '+title,'HACKING',win32con.MB_OK)
            try:
                #os.system(title)
                Popen(title,shell=True,stdout=PIPE,stderr=PIPE)  #用Popen代替os，避免弹出黑框
            except Exception,e:
                pass
            title
        time.sleep(3)
