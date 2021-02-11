#coding=utf-8
'''
假设lrc歌词文件中，翻译与原文都是在同一个时刻上（应该都是吧
author: Tmn07
'''
import re

f = open('test.lrc', 'r', encoding='utf-8')

data = f.read()

positions = ["{\pos(800,1030)}", "{\pos(80,900)}"]
K = 1
count = 0
translate = 0
# 提前出现与消失延后时间 使用aegisub来调整
# pre = 0.8
# post = 0.8

result = {}
times = []
for line in data.split('\n'):
	# 00:09.36
	match_list = re.findall('\[\d*?:\d*?\.\d*?]', line)
	if match_list:
		for m in match_list:
			# print(m)
			tmp = result.get(m)
			if tmp!=None:
				if tmp == "" or line[len(line)-line[::-1].index(']'):] == "//": ## qq music中 翻译空白区 与 部分不翻译时用//来替代
					continue
				else:
					# lrc
					if translate:
						result[m] = tmp + "\n" + line[len(line)-line[::-1].index(']'):]
			else:
				if K:
					offset = positions[count]
					count = 1 if count == 0 else 0
				else:
					offset = ''
				result[m] = offset+line[line.index(']')+1:]
				times.append(m)
	else:
		continue

f.close()
def maketime(start ,end):
	# 00: 一小时以内的轴..
	if start == 0:
		ss = '00:00:00,000'
	else:
		ss = "00:"+start[1:-1].replace('.',',')+"0"
	se = "00:"+end[1:-1].replace('.',',')+"0"
	return ss + " --> " + se

times.sort()

with open("result.lrc", 'w', encoding='utf-8') as f:
	with open("result.srt", 'w', encoding='utf-8') as f2:

		pretime = times[0]
		# for ind in range(1,len(times)):
		for ind in range(1,len(times)+1):
			f2.write(str(ind)+"\n")
			# 用于处理最后一条歌词信息
			if ind==len(times):
				f2.write(maketime(pretime, pretime)+"\n")
			else:
				f2.write(maketime(pretime, times[ind])+"\n")
				pretime = times[ind]
			f2.write(result[times[ind-1]]+"\n\n") 
		
		# lrc
		for t in times:
			f.write(t+result[t]+"\n") 




