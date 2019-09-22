"""
学习Python的记录
wang daka
..........
..........
"""
print("Languages:\nPython\nC\nJAVA")     #换行符
print("\n")                              #注意用法

print("\tpython")                        #制表符


favourite_language = ' Python '
print (favourite_language.rstrip())      #删去末尾空白(暂时的)未改变字符串本身
favourite_language2 = favourite_language.lstrip()#删去前面空白
favourite_language3 = favourite_language.strip()#删去两端空白
print(favourite_language3)



name = "Joe"
print("Hello " + name + ' , would you like to learn some Python today ?')

first_name = 'ada'
last_name = 'lovelace'
full_name = first_name + ' ' + last_name
print('Hello ' + full_name.title() + "!")       #首字母大写
print(full_name.upper())                        #全部大写
print(full_name.lower())                        #全部小写

print('Albert Einstein once said,"A person who never made a mistake never tried anything new !"')



age = 23
message = "Happy " + str(age) + "rd Birthday!"  #注意字符的格式
print(message)
print(5 + 3)
print(2 * 4)
print(10 - 2)
print(int(40 / 5))
