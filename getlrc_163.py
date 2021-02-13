#coding=utf-8

import requests, json

mid = '455502443'

url = "http://music.163.com/api/song/lyric?os=pc&id="+mid+"&lv=-1"

with_translate = "&tv=-1"

headers = {
	'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}


r = requests.get(url+with_translate, headers=headers)

jsondata = json.loads(r.text)

with open('test.lrc', 'w', encoding='utf-8') as f:
	f.write(jsondata['lrc']['lyric'])
	if jsondata['tlyric'].get('lyric'):
		f.write(jsondata['tlyric']['lyric'])
	else:
		print ('no translate version')
	print ('Finish')
