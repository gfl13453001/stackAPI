from stackNoteAPI.settings.dev import QN_OSS

from qiniu import Auth, put_file, etag
import qiniu.config

from common.main import md5


def upload(filename,path):
    #需要填写你的 Access Key 和 Secret Key
    access_key = QN_OSS["Access_Key"]
    secret_key = QN_OSS["Secret_Key"]

    #构建鉴权对象
    q = Auth(access_key, secret_key)

    join_path = path.split('\\')[-1].split('.')[-1]
    # 要上传的空间
    bucket_name = QN_OSS["space"][0]

    #上传后保存的文件名
    fileName_os = f'{md5(filename)}.{join_path}'

    #生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket=bucket_name,expires=3600)

    #要上传文件的本地路径

    ret, info = put_file(token, fileName_os, path,version="v2")

    reJson = {
        "ret":ret,
        "info":info,
        "file":{
            "url":QN_OSS["url"]+"%s"%fileName_os,
            "name":fileName_os,
            "type":join_path
        }

    }


    return reJson




# access_key = QN_OSS["Access_Key"]
# secret_key = QN_OSS["Secret_Key"]
# from qiniu import Auth
# q = Auth(access_key, secret_key)
# print(q.)
