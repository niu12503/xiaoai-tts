# -*- coding: utf-8 -*-
import requests
import urllib

# Cookie通过抓取小爱音箱数据获取

binUrl = "https://bigota.miwifi.com/xiaoqiang/rom/s12a/mico_all_f86a5_1.44.4.bin"
# 自行替换低版本文件地址

headers = {
    "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
    "Connection": "keep-alive",
    "Cookie": "userId=userId;serviceToken=serviceToken==;cUserId=cUserId;deviceId=deviceId;sn=sn",
    "Accept-Language": "zh-cn",
    "User-Agent": "MiSoundBox/2.0.41 CFNetwork/978.0.7 Darwin/18.5.0",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache"
}

bodydata = {
    "checksum": "00c355fbae2104aa6051aa34893f86a5",
    "deviceId": "deviceId",
    "extra": '{"cfe":1000002,"linux":1,"rootfs":1,"weight":1,"sqafs":1,"ramfs":1}',
    "hardware": "S12A",
    "requestId": "xxxx",
    "url": binUrl,
    "version": "1.44.4"
 }

body = urllib.parse.urlencode(bodydata)
url = "https://api.mina.mi.com/remote/ota/v2"
response = requests.post(url, data=body, headers=headers)
print(response.text)
# 成功返回内容 {"code":0,"message":"Success","data":""}
