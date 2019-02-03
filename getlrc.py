#coding=utf-8
'''
这篇文章原址可能不能访问了，API参考：http://get.ftqq.com/7430.get
author: Tmn07
'''

import requests, json

mid = '460099384'

url = "http://music.163.com/api/song/lyric?os=pc&id="+mid+"&lv=-1"

with_translate = "&tv=-1"

headers = {
	'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}


r = requests.get(url+with_translate, headers=headers)

jsondata = json.loads(r.text)

with open('test.lrc', 'w') as f:
	f.write(jsondata['lrc']['lyric'].encode('utf-8'))
	if jsondata['tlyric'].get('lyric'):
		f.write(jsondata['tlyric']['lyric'].encode('utf-8'))
	else:
		print ('no translate version')
	print ('Finish')
