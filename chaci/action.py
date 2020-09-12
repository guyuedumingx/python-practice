import requests
from bs4 import BeautifulSoup 
import review

# 从网络查词  
def getWord(word):
    url = "https://cn.bing.com/dict/search"
    kv = {'q':word}
    try:
        r = requests.get(url, params=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("网络连接错误...")
        print("您可以查询单词库中的单词...")
        return ""

# 解析网页  
def parssWord(html,word,dict_word):
    soup = BeautifulSoup(html, "html.parser")
    for info in soup.find_all("meta"):
        try:
            if (info.attrs['name'] == 'description'):
                dict_word[word] = [4, info.attrs['content']] 
        except:
            continue


# 打印单词
def printWord(dict_word, word):
    try:
        info = dict_word[word][1].split('，')
    except:
        try: 
            info = dict_word[1].split('，')
        except:
            pass
    for i in info[1:]:
        for g in i.split(' '):
            print(g)
    print("------------------------------------------------------")

# 检测输入  
def judge(word_book, c):
    if (c == 'w'):
        for key in word_book.keys():
            print('\n' + key + ' :')
            printWord(word_book, key)
        
    elif (c == 'q'):
        print("退出软件...")
        return False

    elif (c == 'd'):
        for key in word_book.keys():
            print(key + '\t')
        name = input("删除单词: ") 
        if (name == 'q'):
            return False 
        try:
            del word_book[name.strip()]
            print("已删除" + name)
        except:
            print("没有这个单词!!!")
    elif (c == 'r'):
        review.reWord(word_book)
         
    else:
        if c in word_book.keys():
            printWord(word_book[c], c)
        else:
            html = getWord(c)
            if (html != ""):
                parssWord(html, c, word_book)
                printWord(word_book, c) 
    return True 

