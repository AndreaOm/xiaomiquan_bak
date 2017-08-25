import json
import time
import requests
from urllib import quote

token = '84E9416F-9B3A-73B7-4966-AEA7FB10B729' # Your access_token
name = 'xxx' # Your name
user_id = '0000000000000' # Your user_id
avatar_url = 'https://file.xiaomiquan.com/201612/xxx.jpg' # Your avatar_url


headers = {
    'Host': 'wapi.xiaomiquan.com',
    'Origin': 'https://wx.xiaomiquan.com',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'authorization': token,
    'Accept': '*/*',
    'Referer': 'https://wx.xiaomiquan.com/dweb/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.'+str(time.strftime('%S',time.localtime(time.time()))),
    'Connection': 'keep-alive',
    'x-request-id': '92c35538-be75-3029-4d8a-e338e6'+str(time.strftime('%H%M%S',time.localtime(time.time())))
}

cookies = {
    'access_token': token,
    'name': name,
    'user_id': user_id,
    'PHPSESSID': '42g23c6ss7140joq3mmsb114t2',
    'UM_distinctid': '15d59be81a811b-0e2bd99982822d8-7f682331-1fa400-15d59be81a930f',
    'ws_address': 'ws_address=wss%3A//ws.xiaomiquan.com%3A443/ws%3Fversion%3Dv1.6%26access_token%3D'+token,
    'avatar_url': avatar_url
}


api = 'https://wapi.xiaomiquan.com/v1.6/'


def saveTopics(groupId):
    o = getAllTopics(groupId,getTimeNow())
    with open(str(time.strftime('%Y%m%d',time.localtime(time.time()))) + '-' + str(groupId) + '.json','wb+') as f:
        f.write(json.dumps(o))

def getTopicsByTime(groupId,t):
    time.sleep(1)
    return requests.get(api + 'groups/' + str(groupId) + '/topics?count=20&end_time=' + quote(t), headers=headers , cookies=cookies)

def getEndTime(o):
    return o['resp_data']['topics'][len(o['resp_data']['topics'])-1]['create_time']

def getTimeNow():
    return str(time.strftime('%Y-%m-%dT%H:%M:%S.6%S+0800',time.localtime(time.time())))

def getAllTopics(groupId,t):
    d = []
    n = (getTopicsNums(groupId)/20+1)
    for x in range(n):
        c = getTopicsByTime(groupId, t)
        t = getEndTime(json.loads(c.content))
        d.extend(json.loads(c.content)['resp_data']['topics'])
    return d

def getTopicsNums(groupId):
    return json.loads(requests.get(api + 'groups/' + str(groupId) + '/details', headers=headers , cookies=cookies).content)['resp_data']['group']['statistics']['topics']['topics_count']

saveTopics(2212251881) # set bakup group id
saveTopics(1852214142)
saveTopics(5421844144)
