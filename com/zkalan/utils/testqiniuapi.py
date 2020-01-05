# -*- coding: utf-8 -*-
# flake8: noqa
from qiniu import Auth, put_file
from readsettings import get_all_config
import qiniu.config

if __name__ == '__main__':

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
    key = com_prefix + '七牛云多媒体处理图片基本免费.PNG'

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
    localfile = 'C:\\Users\\zhangkai\\Desktop\\blog\\images\\七牛云多媒体处理图片基本免费.PNG'
    ret, info = put_file(token, key, localfile)
    print(type(ret))
    print(type(info))
