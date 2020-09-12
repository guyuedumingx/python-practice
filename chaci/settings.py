import os
import json 



root = "/home/harden/learn/chaci/"

# 打开文件  
def open_file(file_name):
    path = root + file_name 

    # 如果没有该目录，则创建该目录  
    if not os.path.exists(root):
        os.mkdir(root)

    # 加载单词本  
    try:
        with open(path, encoding='utf-8-sig', errors='ignore') as f:
            return json.load(f, strict=False)

    # 如果没有单词本，则返回空字典做为新字典 
    except:
        return {}  

# 保存文件  
def save_file(word_book, file_name):
    path = root + file_name
    with open(path, 'w') as f:
        json.dump(word_book, f)
