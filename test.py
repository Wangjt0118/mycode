# 阿里云短信
from hashlib import sha1
import datetime
import requests
import json
import base64
import hmac
import uuid
import urllib
import hashlib


def send_messages(params):
    AccessKeySecret = ''

    # 公共参数
    params.update({
        "AccessKeyId": "",
        "Format": "json",
        "RegionId": "cn-hangzhou",
        "SignatureMethod": "HMAC-SHA1",
        "SignatureNonce": str(uuid.uuid4()),
        "SignatureVersion": "1.0",
        "Timestamp": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "Version": "2017-05-25",
    })
    if "Signature" in params:
        params.pop("Signature")

    dict = sorted(params.items(), key=lambda x: x[0])

    # 按规定格式转码拼接
    # 签名
    sign = ""
    for key, value in dict:
        sign += "&" + URLcoder(key) + "=" + URLcoder(value)
    sign = sign[1:]
    stringToSign = 'GET' + '&' + URLcoder('/') + "&" + URLcoder(sign)

    AccessKeySecret = AccessKeySecret + '&'
    signature = base64.b64encode(hmac.new(AccessKeySecret.encode("utf8"), stringToSign.encode("utf8"), digestmod=hashlib.sha1).digest())
    params['Signature'] = signature.decode()
    return params


# 格式转换
def URLcoder(String):
    return urllib.parse.quote(String, ' ').replace('+', '%20').replace('*', '%2A').replace('%7E', '~')


# 发送短信.入口
def sendmessages():
    destUrl = 'https://dysmsapi.aliyuncs.com/'
    headers = {'content-type': 'application/json'}
    params = {
        "Action": "SendSms",
        "PhoneNumbers": "",
        "SignName": "复星iHR",
        "TemplateCode": "SMS_187951124",
        "TemplateParam": "{\"name\":\"翁樟韬123\"}",
    }
    params = send_messages(params)
    destUrl = destUrl
    print (destUrl, params)
    r = requests.post(destUrl, params=params, headers=headers)
    # 打印结果
    print (r.text)
sendmessages()
