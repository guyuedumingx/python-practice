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

## BeautifulSoup  
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
> 迭代类型用在for in 中  

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
平行遍历发生在同一个父节点下的各节点间  

|属性|说明|
|---|---|
|.next_sibling|返回按照HTTP文本顺序的下一个平行节点标签|
|.previous_sibling|返回按照HTML文本顺序的上一个平行节点标签|
|.next_siblings|迭代类型，返回按照HTML文本顺序的后续所有平行节点标签|
|.previous_siblings|迭代类型，返回按照HTML文本顺序的前续所有平行节点标签|

迭代类型只能用在*for / in* 类型中  

```python
>>> soup = BeautifulSoup(demo, "html.parser")
>>> soup.a.next_sibling
' and '
>>> soup.a.next_sibling.next_sibling
<a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>
>>> soup.a.previous_sibling
'Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:\r\n'
>>> soup.a.previous_sibling.previous_sibling
>>> soup.a.parent
<p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a> and <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>.</p>
```
#### bs4的prettify()方法  
```python
>>> soup = BeautifulSoup(demo, "html.parser")
>>> soup.prettify()
>>> print(soup.a.prettify())
<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">
 Basic Python
</a>
```
#### JSON
```JSON
"key" : "value"
"key" : ["value1","value2"]
"key" : {"subkey" : "subvalue"
		"subkey2" : "subvalues2"}
```
#### YAML  
用 缩进 来表达所属信息  
用 - 来表达并列关系  
用 | 表示整块数据    
```YAML
name : 
	newName : 你好  
	oldName : Hello  
key : 
	subkey : subvalue
good : 			#表达并列关系  
-北京理工大学  
-延安自然科学院  

# |表示整块数据
text: |		#学校介绍
北京理工大学创立于～～～

```



#### <>.find_all(name,attrs,recursrve,string,**kwargs)
返回一个列表，储存查找的结果   
name: 对标签名称的检索字符串  
attrs: 对标签属性值的检索字符串，可标注属性检索  
recursive: 是否对子孙全部检索，默认为True,如果为False，则只对儿子节点检索  
string: <>...</>中字符串区域的检索字符串  


```python 
# 查找a标签  
soup.find_all('a')

# 查找a和b标签  
# 把a和b作为第一个参数，用列表形式传输  
soup.find_all(['a','b'])

# 若参数为True则给出所有标签的信息
for tag in soup.find_all(True):
	print (tag.name)

#只显示以b开头的标签  
import re		#正则表达式库
for tag in soup.find_all(re.compile('b')):
	print (tag.name)

# 检索带有course属性值的标签  
soup.find_all('p','course')
[<p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
<a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">Basic Python</a> and <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">Advanced Python</a>.</p>]

# 查找id值为link1的标签
soup.find_all(id='link1')

# 查找以link开头的标签 
import re
soup.find_all(id=re.compile('link'))

# string  
soup.find_all(string = "Basic Python")
['Basic Python']

# 检索带有python的字符串  
import re
soup.find_all(string = re.compile("python"))
['This is a python demo page', 'The demo python introduces several python courses.']

>>> for link in soup.find_all('a'):
...     print(link.get('href'))
http://www.icourse163.org/course/BIT-268001
http://www.icourse163.org/course/BIT-1001870001
>>>

```


> < tag>(..)等价于 < tag>.find_all(..)   
> soup.(..)等价于 soup.find_all(..)   

|方法|说明|  
|----|----|  
|<>.find()|搜索且只返回一个结果，字符串类型，同.find_all()参数|
|<>.find_parents()|在父辈节点中搜索，返回列表类型，同.find_all()参数|
|<>.find_parent()|在父辈节点中返回一个结果，字符串类型，同.find()参数|
|<>.find_next_siblings()|在后续平行节点中搜索，返回列表类型，同.find_all()参数|
|<>.find_next_sibling()|在后续平行节点中返回一个结果，字符串类型，同.find()参数|
|<>.find_previous_siblings()|在前序平行节点中搜索，返回列表类型，同.find_all()参数|
|<>.find_previous_sibling()|在前序平行节点中返回一个结果，字符串类型，同.find()参数|


### 实例  
#### 中国大学定向排名  
- 保存在*universityRaw.py*中  

-------------------
## 正则表达式 RE   

> 通用的字符串表达框架  
> 简洁表达一组字符串的表达式  
> 针对字符串表达“简介”和“特征”思想的工具  

1. 表达文本特征  
2. 同时查找或替换一组字符串  
3. 匹配字符串的全部或部分   

*正则表达式需要编译*   

|操作符|说明|实例|
|-----|-----|----|
|.|表示单个字符||
|[]|字符集，对单个字符给出取值范围|[abc]表示a、b、c,[a-z]表示a到z单个字符|
|[^]|非字符集，对单个字符给出排除范围|[^abc]表示非a或b或c的单个字符|
|*|前一个字符0次或无线次拓展|abc*表示ab、abc、abcc、abccc等|
|+|前一个字符表示一次或无线次拓展|abc+表示abc、abcc、abccc等|
|?|前一个字符0次或1次拓展|abc?表示ab、abc|
|xx&#124;xx|左右表达式任意一个|abc&#124;def表示abc、def|
|{m}|扩展一个字符m次|ab{2}c表示abbc|
|{m,n}|扩展前一个字符m至n次(含n)|ab{1,2}c表示abc、abbc|
|^|匹配字符串开头|^abc表示abc且在一个字符串的开头|
|$|匹配字符串结尾|abc$表示abc且在一个字符串的结尾|
|()|分组标记，内部只能使用&#124;操作符|(abc)表示abc,(abc&#124;def)表示abc、def|
|\d|数字，等价于[0-9]||
|\w|单词字符，等价于[A-Za-z0-9_]||

|正则表达式|对应字符串|
|----------|----------|
|PP(Y&#124;YT&#124;YTH&#124;YTHO)?N|'PPN'、'PPYN'、'PPYTN'、'PPYTHN'、'PPYTHON'|
|PYTHON+|'PYTHON'、'PYTHONN'、'PYTHONNN'、……|
|PY[TH]ON|'PYTON'、'PYHON'|
|PY[^TH]?ON|'PYON'、'PYaON'、'PYbON'、'PYcON'、……|
|PY{:3}N|'PN'、'PYN'、'PYYN'、'PYYYN'|
|^[A-Za-z]+$|仅由字母组成的字符串|
|^[A-za-z0-9]+$|由字母和数字组成的字符串|
|^-?\d+$|由整数组成的字符串|
|^[0-9]\*[1-9][0-9]\*$|正整数形式的字符串|
|[1-9]\d{5}|中国境内邮政编码，6位|
|[\u4e00-\u9fa5]|匹配中文字符(UTF-8)|
\d{3}-\d{8}|\d{4}-\d{7}	国内电话号码，010-68913536   

##### 精确写法： 
|范围|表达方法|
|----|--------|
|0-99| [1-9]?\d|
|100-199|1\d{2}|
|200-249|2[0-4]\d|
|250-255|25[0-5]|

> 表示IP地址的正则表达式：  
(([1-9]?\d|1\d{2}|2[0-4]\d|25[0-5]).){3}([1-9]?\d|1\d{2}|2[0-4]\d|25[0-5])
 
当正则表达式中出现转义符\时使用raw string(原生字符串)类型(只需要在字符串前面加r)  

|函数|说明|
|----|----|
|re.search()|在一个字符串中搜索匹配正则表达式的第一个位置，返回match对象|
|re.match()|从一个字符串的开始位置起匹配正则表达式，返回match对象|
|re.findall()|搜索字符串，以列表类型返回全部能匹配的子串|
|re.split()|将一个字符串按照正则表达式匹配结果进行分割，返回列表类型|
|re.finditer()|搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素是match对象|
|re.sub()|在字符串中替换所有匹配正则表达式的子串，返回替换后的字符串|

#### re.search(pattern, string, flags=0)    

在字符串中搜索匹配正则表达式的第一个位置，返回match对象  
- pattern: 正则表达式的字符串或原生字符串表示  
- string: 待匹配的字符串  
- flags: 正则表达式使用时的控制标记  

|常用的flags|说明|
|-----------|----|
|re.I re.IGNORECASE|忽略正则表达式的大小写，[A-Z]能够匹配小写字符串|
|re.M re.MULTILINE|正则表达式中的^操作符能够将给定字符串的每行当作匹配开始|
|re.S re.DOTALL|正则表达式中的.操作符能够匹配所有字符(默认匹配除换行符外的所有字符)|

```python
>>> import re
>>> match = re.search(r'[1-9]\d{5}', 'BIT 100081')
>>> if match:
		print(match.group(0))
100081
>>>
```

#### re.match(pattern, string, flags=0)
从一个字符串的开始位置起匹配正则表达式，返回match对象  

```python

# match是从头开始匹配的，如果头部不符合，则返回空字符串  
>>> match = re.match(r'[1-9]\d{5}', '100081 BIT')
>>> if match:
	     match.group(0)

'100081'
>>>
```

#### re.findall(pattern, string, flags=0)  
搜索字符串，以列表类型返回全部能匹配的子串  
```python
>>> ls = re.findall(r'[1-9]\d{5}', 'BIT100081 TSU100084')
>>> ls
['100081', '100084']
```

#### re.split(pattern, string, maxsplit=0, flags=0)
将一个字符串按照正则表达式匹配结果进行分割，返回列表类型  
- maxsplit: 最大分割数，剩余部分作为最后一个元素输出  

```python
>>> re.split(r'[1-9]\d{5}', 'BIT100081 TSU100084', maxsplit=1)
['BIT', ' TSU100084']
>>> re.split(r'[1-9]\d{5}', '100081BIT 100084TSU', maxsplit=1)
['', 'BIT 100084TSU']

```

#### re.finditer(pattern, string, flags=0) 
搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素是match对象  

```python
>>> for m in re.finditer(r'[1-9]\d{5}', 'BIT100081 TSU100084'):
		if m:
			print(m.group(0))  
100081
100084
```
#### re.sub(pattern, repl, string, count=0, flags=0)
在一个字符串中替换所有匹配正则表达式的子串，返回替换后的字符串  
- repl: 替换匹配字符串  
- count: 匹配的最大替换次数  

```python
>>> re.sub(r'[1-9]\d{5}',':zipcode', 'BIT100081 TSU100084')
'BIT:zipcode TSU:zipcode'
```

```python
# Re库的函数式用法(一次性操作)  
>>> rst = re.search(r'[1-9]\d{5}', 'BIT 100081')

# 面向对象用法：编译后的多次操作  
>>> pat = re.compile(r'[1-9]\d{5}')
>>> rst = pat.search('BIT 100081')  

```



#### regex = re.compile(pattern, flags=0)  

> 将正则表达式的字符串形式编译成正则表达式对象(可多次使用)  
正则表达式的字符串或原生字符串并不是正则表达式  
编译过后的regex(pat类型)才是  
regex对象可以使用正则表达式库的6种函数  

|函数|说明|
|----|----|
|regex.search()|在一个字符串中搜索匹配正则表达式的第一个位置，返回match对象|
|regex.match()|从一个字符串的开始位置起匹配正则表达式，返回match对象|
|regex.findall()|搜索字符串，以列表类型返回全部能匹配的子串|
|regex.split()|将一个字符串按照正则表达式匹配结果进行分割，返回列表类型|
|regex.finditer()|搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素是match对象|
|regex.sub()|在字符串中替换所有匹配正则表达式的子串，返回替换后的字符串|

#### Re库的match对象  
单次匹配的结果  

|属性|说明|
|----|----|
|.string|待匹配的文本|
|.re|匹配时使用的pattern对象(正则表达式)|
|.pos|正则表达式搜索文本的开始位置|
|.endpos|正则表达式搜索文本的结束位置|


|方法|说明|
|----|----|
|.group(0)|获得匹配后的字符串|
|.start()|匹配字符串在原始字符串的开始位置|
|.end()|匹配字符串在原始字符串的结束位置|
|.span()|返回(.start(),.end())|

> 还有group(1)等方法  

#### 实例  

```python
>>> import re
>>> m = re.search(r'[1-9]\d{5}', 'BIT100081 TSU100084')
>>> m.string
'BIT100081 TSU100084'
>>> m.re
re.compile('[1-9]\\d{5}')
>>> m.endpos
19
>>> m.pos
0
>>> m.group(0)
'100081'
>>> m.start()
3
>>> m.end()
9
>>> m.span()
(3, 9)
```

#### Re库的贪婪匹配和最小匹配  

```python
# 贪婪匹配，即输出匹配最长的字串

>>> match = re.search(r'PY.*N', 'PYANBNCNDN')
>>> match.group(0)
'PYANBNCNDN'

# 最小匹配  
>>> match = re.search(r'PY.*?N', 'PYANBNCNDN')>>> match.group(0)
'PYAN'
```
> 在操作符后面加？号来获得最小匹配的结果

|操作符|说明|
|------|----|
|\*?|前一个字符0次或无线次扩展,最小匹配|
|+?|前一个字符1次或无线次扩展,最小匹配|
|??|前一个字符0次或1次扩展,最小匹配|
|{m,n}?|扩展前一个字符m至n次(含n),最小匹配|
