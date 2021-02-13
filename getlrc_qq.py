#coding=utf-8

import requests, json
import re

########## 分享短链接跳转#########
url = "https://c.y.qq.com/base/fcgi-bin/u?__=UxGmt3g"

r = requests.get(url)
matchs = re.findall('mid&#61;.*?&#38;no_redirect', r.text)

sid = matchs[0][8:-16]

get_para = {
    "songmid" : sid,
    "g_tk"    : 5381,
    "format"  : "json",
    "nobase64": 1
}


headers = {
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    "Referer":"https://y.qq.com/portal/player.html"
}

url = "https://c.y.qq.com/lyric/fcgi-bin/fcg_query_lyric_new.fcg"



r = requests.get(url, params=get_para, headers=headers)

jsondata = json.loads(r.text)



with open('test.lrc', 'w', encoding='utf-8') as f:
    f.write(jsondata['lyric'])
    if jsondata.get('trans'):
        f.write(jsondata['trans'])
    else:
        print ('no translate version')
    print ('Finish')



