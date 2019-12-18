import requests
import os
root = "/home/harden/python-practice/requests_learn/"
url = "https://m3u8.40cdn.com/videos/ajvs/1910/5tTduh7g/hls/5tTduh7g.m3u8"
path = root + url.split('/')[-1]
try:
	if not os.path.exists(root):
		os.mkdir(root)
	if not os.path.exists(path):
		r = requests.get(url)
		with open(path, 'wb') as f:
			f.write(r.content)
			f.close()
			print("文件保存成功")
	else:
		print("文件已存在")
except:
	print("爬取失败")
