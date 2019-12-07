## Requests   
#### requests.get (url, params=None, **kwargs)

> url: 拟获取页面的url链接  
> params: url中的额外参数，字典或字节流格式，可选  
> **kwargs: 12个控制访问的参数  

```python
import requests
url = "http://www.baidu.com"
r = requests.get(url)
print(r.status_code)
```

> r.status_code: HTTP请求的返回状态，200表示成功，404表示失败  
> r.text: HTTP响应内容的字符串形式，即，url对应的页面内容  
> r.encoding: 从HTTP header中猜测的响应内容的编码方式  
> r.apparent_encoding: 从内容分析出相应内容的编码方式（备选编码方式）  
> r.content: HTTP响应内容的二进制形式  

如果文件显示不正确，可以：  

```python
r.encoding = r.apparent_encoding
```

#### 理解Requests库的异常  

|异常|说明|
|----|----|
|requests.ConnectionError| 网络连接错误异常,如DNS查询失败,拒绝连接等|  
|requests.HTTPError| HTTP错误异常|  
|requests.URLRequired| URL缺失异常|  
|requests.TooManyRedirects| 超过最大重定向次数，产生的重定向异常|  
|requests.ConnestTimeout| 连接远程服务超时异常|  
|requests.Timeout| 请求URL超时，产生超时异常|  

------

#### 爬取网页的通用代码框架  
> 可以用raise_for_status方法来处理异常  

```python
import requests

def getHTMLText(url):
	try:
		r = requests.get(url, timeout=30)
		r = raise_for_status() #如果状态不是200,引发HTTPError异常
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return "产生异常"

if __name__ == "__main__":
	url = "http://www.baidu.com"
	print(getHTTPText(url))
```
|  HTTP方法  |  说明  |
|  :--:  |  ---   | 
|GET|请求URL位置的资源|
|HEAD|请求页面的头部信息|
|POST|请求向URL位置的资源后附加新的数据|
|PUT|请求向URL位置存储一个资源，覆盖原URL位置的资源|
|PATCH|请求局部更新URL位置的资源，即改变该处资源的部分内容|
|DELETE|请求删除URL位置存储的资源|

> HTTP的方法和requests库的方法是一一对应的  
> HEAD 即 requests.head(url)  

```python  
import requests

url = 'http://httpbin.org/get'
r = requests.head(url)  
print(r.headers)  #r.headers展示头部信息

#POST的方法  
#附加字符ABC 自动存入data字段下   
r = requests.post('http://httpbin.org/post', data = 'ABC')
print(r.text)

#附加字典会自动放入from(表单)中
payload = {'keys1': 'value1', 'keys2': 'value2'}
r = requests.post('http://httpbin.org/post', data = payload)
print(r.text)
```
#### Requests库的基本方法  
requests.request (method, url, **kwargs)  

> **kwargs: 控制访问的参数，均为可选项  
> params: 字典或字节序列，作为参数增加到url中  

```python 

# params 对URL进行修改
kv = {'key1': 'value1', 'key2': 'value2'}
r = requests.request('GET', 'http://python123.io/ws', params=kv)
print(r.url)

# data 字典/字节序列/文件对象  
r = requests.request('POST', 'http://python123.io/ws', data=kv)
body = '主体内容'
r = requests.request('POST', 'http://python123.io/ws', data=body)

# json
r = requests.request('POST', 'http://python123.io/ws', json=kv)

# headers 字典，HTTP定制头
hd = {'user-agent': 'Chrome/10'}   # 修改user-agent为Chrome/10
r = requests.request('POST', 'http://python123.io/ws', headers=hd)

# cookies  解析字典或CookieJar，Requests中的cookie 
# auth
 
# files 字典类型，传输文件
fs = {'file': open('data.xls', 'rb')}
r = requests.request('POST', 'http://python123.io/ws', files=fs)
# 向某一个链接提交某一个文件  

# timeout 设定超时时间，秒为单位 
r = requests.request('GET', 'http://wwww.baidu.com', timeout=10)

# proxies 字典类型，设定访问代理服务器，可以增加登录认证
pxs = { 'http': 'http://user:pass@10.10.10.1:1234'
		'https': 'https://10.10.10.1:4321'	}
r = requests.request('GET', 'http://www.baidu.com', proxies=pxs)

# allow_redirects: True/False, 默认为True，重定向开关
# stream: True/False, 默认为True, 默认内容立即下载开关 
# verify: True/False, 默认为True，认证SSL证书开关

# cert: 本地SSL证书路径

```


```python 
import requests

requests.request(method, url, **kwargs)
requests.post(url, data=None, json=None, **kwargs) 
requests.head(url, **kwargs)
requests.put(url, data=None, **kwargs)
requests.patch(url, data=None, **kwargs)
requests,delete(url, **kwargs)
requests.get (url, params=None, **kwargs)
# data: 字典，字节序列，文件，Request的内容  
# json: JSON格式的数据，Request的内容  
# **kwargs: 11个控制访问的参数  
# post,put,patch,delete很难成功

```

#### 网络爬虫的尺寸   
|爬取网页 玩转网页|爬取网站 爬取系列网站|爬取全网|
|:-------:|:---:|:----:|
|小规模，数据量小 爬取速度不敏感|中规模，数据规模较大 爬取速度敏感|大规模，搜索引擎 爬取速度关键|
|Request库|Scrapy库|定制开发|

#### Robots协议  
**Robots Exclusion Standdard**  网络爬虫排除标准  
作用： 告知爬虫哪些页面可以爬取，哪些不行   
形式： 在网站根目录下的*robots.txt*文件  
不是所有的网站都有*robots.txt*文件,对于这些网站，可以爬取全部网页  


### 实例 

**爬取京东**  
```python
>>> import requests
>>> r = requests.get("https://item.jd.com/2967929.html")
>>> r.status_code
200
>>>r.encoding
'gbk'
>>> r.text[:1000]

```
**爬取亚马逊**

```python
>>> r = requests.get("https://www.amazon.cn/gp/product/B01M8L5Z3Y")
>>> r.status_code
503
>>> r.encoding
'ISO-8859-1'
>>> r.encoding = r.apparent_encoding
>>> r.request.headers
{'User-Agent': 'python-requests/2.22.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}

# 模拟浏览器Mozilla/5.0登录
>>> kv = {'User-agent':'Mozilla/5.0'}
>>> r = requests.get(url, headers = kv)
>>> r.status_code
200
>>> r.request.headers
{'User-agent': 'Mozilla/5.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}

```
**百度360搜索关键词提交** 
> 百度的关键词接口：  
> http://www.baidu.com/s?wd=keyword  
> 360的关键词接口：  
> http://www.so.com/s?q=keyword  

```python

>>> import requests

# baidu
>>> kv = {'wd':'python'}
>>> r = requests.get("http://www.baidu.com/s", params=kv)
>>> r.status_code
200


# 360
>>> kv = {'q': 'python'}
>>> r = requests.get("http://www.so.com/s", params=kv)
>>> r.status_code
200
>>> r.request.url
'https://www.so.com/s?q=python'
>>> len(r.text)
349760

```

**网络图片的爬取**  

```python
import requests
import os
url = "https://img.ivsky.com/img/bizhi/pre/201909/25/haitun-004.jpg"
root = "/home/harden/python-practice/requests_learn/"
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
```
以上代码保存在*download_picture.py*中

**实例5：IP地址归属地的自动查询**  
```python 
>>> import requests
>>> url = "http://www.ip138.com/iplookup.asp?ip="
>>> r = requests.get(url + '202.204.80.112')
>>> r.status_code
200

```
---------

### Learn BeautifulSoup  
```python
>>> import requests
>>> from bs4 import BeautifulSoup
>>> r = requests.get("https://python123.io/ws/demo.html")  
>>> demo = r.text
>>> soup = BeautifulSoup(demo, "html.parser")
>>> print(soup.prettify())

```

**BeautifulSoup库的理解**  

```python
>>> from bs4 import BeautifulSoup
>>> soup = BeautifulSoup("<html>data</html>", "html.parser")
>>> soup2 = BeautifulSoup(open("/home/Harden/python_practice/markdown/u.html"), "html.parser")
```

|解析器|使用方法|条件|
|-----|-----|----|
|bs4的HTML解析器|BeautifulSoup(mk,'html.parser')|安装bs4库|
|lxml的HTML解析器|BeautifulSoup(mk,'lxml')|pip install lxml|
|lxml的XML解析器|BeautifulSoup（mk,'xml')|pip install lxml|
|html5lib的解析器|BeautifulSoup(mk,'html5lib')|pip install html5lib|

**BeautifulSoup类的基本元素**  

|基本元素|说明|
|----|----|
|Tag|标签，最基本的信息组织单元，分别用< >和</>表明开头和结尾|
|Name|标签的名字，< p >...< /p>的名字是'p',格式: < tag>.name|
|Attributes|标签的属性，字典形式组织，格式: < tag>.attrs|
|NavigableString|标签内非属性字符串，<>...< />中字符串，格式: < tag>.string|
|Comment|标签内字符串的注释部分，一种特殊的Comment类型|

```python
>>> import requests
>>> from bs4 import BeautifulSoup
>>> r = requests.get("https://python123.io/ws/demo.html")  
>>> demo = r.text
>>> soup = BeautifulSoup(demo, "html.parser")
>>> tag = soup.a  #返回第一个a标签
>>> tag
<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a>
>>> tag.attrs
{'href': 'http://www.icourse163.org/course/BIT-268001', 'class': ['py1'], 'id': 'link1'}
>>> tag.attrs['class']
['py1']
>>> tag.attrs['href']
'http://www.icourse163.org/course/BIT-268001'
>>> type(tag.attrs)
<class 'dict'>
>>> type(tag)
<class 'bs4.element.Tag'>

>>> soup.a.name
'a'
>>> soup.a.parent.name
'p'
>>> soup.p.parent.name
'body'
>>> soup.a
<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a>
>>> soup.a.string
'Basic Python'
>>> soup.p
<p class="title"><b>The demo python introduces several python courses.</b></p>
>>> soup.p.string
'The demo python introduces several python courses.'
>>> type(soup.p.string)
<class 'bs4.element.NavigableString'>

>>> newsoup = BeautifulSoup("<b><!--This is a comment--></b><p>This is not a comment</p>", "html.parser")
>>> newsoup.b.string
'This is a comment'
>>> type(newsoup.b.string)
<class 'bs4.element.Comment'>
>>> newsoup.p.string
'This is not a comment'
>>> type(newsoup.p.string)
<class 'bs4.element.NavigableString'>
```
**标签树的下行遍历**  

|属性|说明|
|---|---|
|.contents|子节点的列表，将< tag>所有的儿子节点存入列表|
|.children|子节点的迭代类型，与.contents类似，用于循环遍历儿子节点|
|.descendants|子孙节点的迭代类型，包含所有子孙节点，用于遍历列表|
> .contents和.children只获得当前节点的子节点信息，而.descendants获得所有的子孙节点

```
>>> soup.head
<head><title>This is a python demo page</title></head>
>>> soup.head.contents
[<title>This is a python demo page</title>]
>>> soup.body.contents
['\n', <p class="title"><b>The demo python introduces several python courses.</b></p>, '\n', <p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a> and <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>.</p>, '\n']
>>> len(soup.body.contents)
5

```
**标签数的上行遍历**  

|属性|说明|
|---|---|
|.parent|节点的父亲标签|
|.parents|节点的父辈标签的迭代类型，用于循环便利父辈节点|
```python
>>> import requests
>>> from bs4 import BeautifulSoup
>>> r = requests.get("https://python123.io/ws/demo.html")  
>>> demo = r.text
>>> soup = BeautifulSoup(demo, "html.parser")

>>> soup.title.parent
<head><title>This is a python demo page</title></head>
>>> soup.html.parent
<html><head><title>This is a python demo page</title></head>
<body>
<p class="title"><b>The demo python introduces several python courses.</b></p>
<p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a> and <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>.</p>
</body></html>
>>> soup.parent # 说明soup的父亲是空的
>>>

```

```python
>>> soup = BeautifulSoup(demo,"html.parser")
>>> for parent in sou.a.parents:
		if parent is None:
			print(parent)
		else:
			print(parent.name)

```

**标签树的平行遍历**  

|属性|说明|
|---|---|
|.next_sibling|返回按照HTTP文本顺序的下一个平行节点标签|
|.previous_sibling|返回按照HTML文本顺序的上一个平行节点标签|
|.next_siblings|迭代类型，返回按照HTML文本顺序的后续所有平行节点标签|
|.previous_siblings|迭代类型，返回按照HTML文本顺序的前续所有平行节点标签|



















