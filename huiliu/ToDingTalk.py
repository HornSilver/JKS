#coding: utf8

import requests
import json
from GetFee import acc,fee

def getDingMes():

    baseUrl = "https://oapi.dingtalk.com/robot/send?access_token=216deebca2c9beec0497d6e359196e7004ff6b943df5ea5b26f9b008090351a9"

    # please set charset= utf-8
    HEADERS = {
        "Content-Type": "application/json ;charset=utf-8 "
    }


    # message = '日期:'+fee['rdate']+',损耗:'+int(fee['fee'])/100+',余额:'+int(acc['accAmount'])/100
    msg = '日期：%s,  损耗:%s,  余额:%s' % (fee['rdate'], int(fee['fee'])/100, int(acc['accAmount'])/100)
    stringBody ={
        "msgtype": "text",
        "text": {"content": msg}
        }

    MessageBody = json.dumps(stringBody)
    result = requests.post(url=baseUrl, data=MessageBody, headers=HEADERS)
    print(result.text)

if __name__ == '__main__':
    getDingMes()
