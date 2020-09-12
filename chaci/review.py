import os
import json
import settings 
from random import randint 

#把单词分为easy, nomal, head
#权重为     1     2       3

def reWord(word_book):
    for word, explain in word_book.items():
        if (explain[0] == 4):
            print(word.strip())
            score = input()
            if (score == '1' or score == 'e' or score == 'j'):
                word_book[word][0] = 1 
            elif (score == '2' or score == 'n' or score == 'k'):
                word_book[word][0] = 2 
            elif (score == '3' or score == 'h' or score == 'l'):
                word_book[word][0] = 3 
    settings.save_file(word_book, 'chaci.json')
