import requests
from bs4 import BeautifulSoup
import re

def getWord(word):
    url = "https://cn.bing.com/dict/search"
    kv = {'q':word}
    try:
        r = requests.get(url, params=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def parssWord(html,word,dict_word):
    soup = BeautifulSoup(html, "html.parser")
    for info in soup.find_all("meta"):
        try:
            if (info.attrs['name'] == 'description'):
                dict_word[word] = info.attrs['content'] 
        except:
            continue 
def printWord(word, dict_word):
    info = dict_word[word].split('，')
    print('\n')
    for i in info:
        for g in i.split(' '):
            print(g)


dict_word = {}
while True:
    word = input("请输入你要查询的单词: ")
    if (word == 'q'):
        print("退出查词！")
        break
    html = getWord(word)
    parssWord(html, word, dict_word)
    printWord(word, dict_word)

