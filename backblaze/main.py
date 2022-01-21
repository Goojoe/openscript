#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：backblaze 
@File    ：last.py
@Author  ：咕咕乔
@Date    ：2022/1/12 17:44
@About   : 一个backblaze服务器备份脚本
'''
'''
安装组件
pip3 install b2sdk py7zr yaml
'''
import b2sdk.v2  # 引入B2SDK模块
import time  # 当前时间
import os  # 文件控制
import shutil  # 移动文件
import py7zr  # 压缩文件夹
import smtplib  # SMTP邮件提醒
import yaml  # 配置文件
# 邮件
from email.mime.text import MIMEText  # 邮件文本处理
from email.header import Header  # 邮件主题

# 变量
with open('config.yaml', 'r') as config:
    configs = dict(yaml.safe_load(config.read()))
    # 文件路径
    webdata = (configs.get('webdata'))
    sqldata = (configs.get('sqldata'))
    timenow = (configs.get('timenow'))
    #认证
    key = (configs.get('key'))
    keyid = (configs.get('keyid'))
    bucketid = (configs.get('bucketid'))
    #SMTP
    from_addr = (configs.get('from_addr'))
    smtp_password = (configs.get('smtp_password'))
    to_addr = (configs.get('to_addr'))
    smtp_server = (configs.get('smtp_server'))
    headline = (configs.get('headline'))
    text = (configs.get('text'))

# 判断文件是否存在
def file_status_mkdir(file_path):
    if os.path.exists(file_path):
        print(file_path + '文件夹存在,X停止创建X')
        return True
    else:
        print(file_path + '文件夹不存在,√创建文件√')
        os.mkdir(file_path)
        return False
file_status_mkdir('upload')
file_status_mkdir('webdata')
file_status_mkdir('sqldata')


# 判断压缩文件夹/文件是否存在
if os.path.exists(flie_path):
    print('你的压缩路径正确,为:\n' + flie_path)
else:
    print('没有找到你的(压缩文件/夹)路径呢?,请检查一下')
    exit()
# 在内存中存储凭证、令牌和缓存
info = b2sdk.v2.InMemoryAccountInfo()
# 账户授权
print("身份验证中,报错请检查网络,Windows关闭系统代理")
b2api = b2sdk.v2.B2Api(info)

# 身份认证
# 执行帐户授权
# -----------------------realm （str）一个授权帐户的领域（通常只是"production"(生产)
b2api.authorize_account("production", keyid, key)

bucket = b2api.get_bucket_by_id(bucketid)  # 返回与给定bucket_id匹配的存储桶
print("压缩文件/夹中")

archive_password = 123456


def size_format(size):  # 构建判断函数
    if size < 1000:
        return '%i' % size + 'B'
    elif 1000 <= size < 1000000:
        return '%.1f' % float(size / 1000) + 'KB'
    elif 1000000 <= size < 1000000000:
        return '%.1f' % float(size / 1000000) + 'MB'
    elif 1000000000 <= size < 1000000000000:
        return '%.1f' % float(size / 1000000000) + 'GB'
    elif 1000000000000 <= size:
        return '%.1f' % float(size / 1000000000000) + 'TB'


def make_archive(zip_name, zip_path, zip_passwd, dst_folder):
    # ----------压缩文件名---文件夹路径--压缩密码----目标路径
    # 判断文件是否存在
    if os.path.exists(zip_path + zip_name):
        print(zip_name + ' 文件/夹存在,X停止压缩X,请检查后删除，或者切换保存路径')
        exit()
    else:
        print(zip_name + ' 文件/夹不存在,√创建压缩√')
    with py7zr.SevenZipFile(zip_name, 'w', password=zip_passwd) as archive:
        # ---------------------文件名-------写权限-密码
        archive.writeall(zip_path)
        # 压缩文件路径，压缩包内文件夹
    shutil.move(zip_name, dst_folder)
    # --移动压缩完成的文件-文件名-目标路径
    bucket.upload_local_file(dst_folder + zip_name, zip_name)

    # 获取文件大小
    fliesize = os.path.getsize(zip_dir + 'unity.7z')

    # 算出文件大小
    fliesize = size_format(zip_name)
    # 转义数字类型为字符串，发邮件及打印日志
    fliesize = str(zip_name)

    if os.path.isfile(dst_folder + zip_name):  # 判断该文件是否为文件或者文件夹
        os.remove(dst_folder + zip_name)  # 若为文件，则直接删除
    return timenow + '：压缩完成,文件名:\n' + zip_name, '在' + dst_folder + '目录下'


print(make_archive('unity.7z', flie_path, '123456', zip_dir))
# 引号里填(桶>桶身份证)

# 压缩文件
# -------------------输出绝对路径---后缀---源文件
# shutil.make_archive(flieoutpath, 'zip', fliezip)


print("上传中")
# 上传文件
# 本地磁盘上文件的路径+新 B2 文件的文件名
# bucket.upload_local_file(upload, b2name)
# print("已上传,文件名为:\n"
#      + b2name + "\n"
#       + "文件大小为:\n"
#       + fliesize)

# SMTP邮件通知设置
# 发送人/用户名

# 邮件信息
msg = MIMEText(text, 'plain', 'utf-8')
# MIMEText（信息,类型,编码)

# 配置
# 发送人
msg['From'] = Header(from_addr)
# 接受人
msg['To'] = Header(to_addr)
# 标题
msg['Subject'] = Header(headline)

# 连接信息
server = smtplib.SMTP()
print('连接SMTP服务器')
server.connect(smtp_server, 25)
# server.connect(服务器,端口)
# port：端口，25，465，587
# 登录
print('登录SMTP服务器')
server.login(from_addr, password)
# uername:用户名
# password:授权码
# 发送邮件
print('发送邮件')
server.sendmail(from_addr, to_addr, msg.as_string())
print('已发送')
# 退出
server.quit()
