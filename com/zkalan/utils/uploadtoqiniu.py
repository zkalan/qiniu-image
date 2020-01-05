# -*- coding: utf-8 -*-
# flake8: noqa
import sys, os
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from qiniu import Auth, put_file
from readsettings import get_all_config


def upload(filepath):
    config = get_all_config()

    # 需要填写你的 Access Key 和 Secret Key
    access_key = config['access_key']
    secret_key = config['secret_key']
    # 构建鉴权对象
    q = Auth(access_key, secret_key)
    # 要上传的空间
    bucket_name = config['bucket_name']
    # 上传后保存的文件名
    com_prefix = config['com_prefix']
    key = com_prefix + filepath.split('/')[-1]

    # 设置转码参数
    fops = config['fops']
    # 转码时使用的队列名称
    pipeline = config['pipeline']

    # 在上传策略中指定
    policy = {
        'persistentOps': fops,
        'persistentPipeline': pipeline
    }
    token = q.upload_token(bucket_name, key, 3600, policy)
    localfile = filepath.replace('/', '\\')
    ret, info = put_file(token, key, localfile)
    print(ret)
    print(info)
    if config['watermark'] == '0':
        # no watermark
        return 'http://' + config['upload_prefix'] + '/' + filepath.split('/')[-1]
    else:
        # watermark
        return 'http://' + config['upload_prefix'] + '/' \
               + config['watermark-file-prefix'] + ret['hash']

