from random import randint


#导入文件
with open('u2.txt') as obj:
    words = obj.readlines()

#实现单词分割
#并把单词与注释保存在key_word
i = 0
key_word = {}

while i < len(words):
    if words[i] == '\n':
        if i < len(words) - 2:
            i = i + 1
        else:
            break
        answer = []
        name = words[i].strip()
        if i < len(words) - 2:
            i = i + 1
        else:
            break
        while words[i] != '\n':
            answer.append(words[i].strip())
            if i < len(words) - 2:
                i = i + 1
            else:
                break
        key_word[name] = answer
    else:
        i = i + 1
        
#实现随机取词  
      
word_name = []
for key in key_word.keys():
	word_name.append(key)

while True:
    inp = input()
    if inp == 'e':
        get = randint(0,len(word_name)-1)
        print(word_name[get])
    if inp == 'q':
        for value in key_word[word_name[get]]:
            print(value)
    
    
    