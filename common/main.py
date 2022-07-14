#!/usr/bin/env python
#-*- coding:utf-8 -*-

# authors:guanfl
# 2021/9/7



import time
import base64
import hmac


import random


def getID(index=60):
    id = ''

    var = '0123456789zxcvbnmasdfghjklqwertyuiopPOIUYTREWQASDFGHJKLMNBVCXZ'

    for i in range(index):
        name = random.choice(var)
        id = name+id

    return id

def get_token(key, expire=18000):
    """
    @Args:
        key: str (用户给定的key，需要用户保存以便之后验证token,每次产生token时的key 都可以是同一个key)
        expire: int(最大有效时间，单位为s)
    @Return:
        state: str
    :param key:
    :param expire:
    :return:
    """
    ts_str = str(time.time() + expire)
    ts_byte = ts_str.encode("utf-8")
    sha1_tshex_str = hmac.new(key.encode("utf-8"), ts_byte, 'sha1').hexdigest()
    token = ts_str+':'+sha1_tshex_str
    b64_token = base64.urlsafe_b64encode(token.encode("utf-8"))

    return b64_token.decode("utf-8")



def certify_token(key, token):
    """
    @Args:
        key: str
        token: str
    @Returns:
        boolean
    :param key:
    :param token:
    :return:
    """
    token_str = base64.urlsafe_b64decode(token).decode('utf-8')
    token_list = token_str.split(':')
    if len(token_list) != 2:
        return False
    ts_str = token_list[0]
    if float(ts_str) < time.time():
        return False
    known_sha1_tsstr = token_list[1]
    sha1 = hmac.new(key.encode("utf-8"), ts_str.encode('utf-8'), 'sha1')
    calc_sha1_tsstr = sha1.hexdigest()
    if calc_sha1_tsstr != known_sha1_tsstr:
        # token certification failed
        return False
    # token certification success
    return True




def b64file(imgPath):
    """用于对图片进行编码为base64、并进行保存到指定的文件中，文件类型是txt
    Args:
        imgPath:图片路径
    Returns:
        example:
    Raises:
    """

    with open(imgPath,"rb") as f:#转为二进制格式
        base64_data = base64.b64encode(f.read())#使用base64进行加密
        #写成文本格式
    return  base64_data




def md5(data):
    """
    md5加密
    """
    import hashlib
    pall = str(data)
    md5_str = hashlib.md5(pall.encode(encoding='UTF-8')).hexdigest()
    return md5_str




#将某文件夹整体复制至指定文件夹
def copy_dir(src_path, target_path):
    if os.path.isdir(src_path) and os.path.isdir(target_path):
        filelist_src = os.listdir(src_path)
        for file in filelist_src:
            path = os.path.join(os.path.abspath(src_path), file)
            if os.path.isdir(path):
                path1 = os.path.join(os.path.abspath(target_path), file)
                if not os.path.exists(path1):
                    os.mkdir(path1)
                copy_dir(path, path1)
            else:
                with open(path, 'rb') as read_stream:
                    contents = read_stream.read()
                    path1 = os.path.join(target_path, file)
                    with open(path1, 'wb') as write_stream:
                        write_stream.write(contents)
        return True

    else:
        return False


import os
import shutil

#将某文件夹下所有文件复制至指定文件夹内，但不复制该文件夹的结构
def copy_dirs(src_path, target_path):
    """copy
    all
    files
    of
    src_path
    to
    target_path"""
    file_count = 0
    source_path = os.path.abspath(src_path)
    target_path = os.path.abspath(target_path)
    if not os.path.exists(target_path):
        os.makedirs(target_path)
    if os.path.exists(source_path):
        for root, dirs, files in os.walk(source_path):
            for file in files:
                src_file = os.path.join(root, file)
                shutil.copy(src_file, target_path)
                file_count += 1
                print(src_file)
    return int(file_count)




class ResponseContent:

    def __init__(self,code,message,data=None,total=None,page=None):
        self.code = code
        self.data = data

        if total:
            self.total = total

        if page:
            self.currentPage = page

        self.message = message







