"""
学习列表
wang daka
..............
..............

"""
names = ['dogs','cats','mouse','cows']
for name in names :                  #遍历列表
    print(name.title())

#反向输出
print(names[-1])                     #输出最后一位
names[0] = 'gods'                    #修改列表的值
print(names)

#添加元素
names.append('friends')              #在列表的最后添加元素
print(names)

i = 5
names = [i] + names
print(names)

names.insert(1,'docadi')             #在列表第二位插入元素
print(names)
#删除元素
del names[0]                         #删去第一位元素
print(names)

#方法remove()只删除第一个值，若列表中存在多个相同的值，需要用循环来删除
names.remove('cats')                 #根据值删除元素
print(names)

"""
while 'cats' in names:
    names.remove('cats')
"""

#删除又使用该元素
unfriend_name = 'cows'
names.remove(unfriend_name)
print("The " + unfriend_name + ' is not friendly !')

print("\n......................\n")

#弹出元素
active_name = []
active_name.append(names.pop())            #弹出元素并同时使用它   
print(active_name)      
print(names)
active_name.append(names.pop(1))           #弹出指定位置的元素
print(active_name)
print(names)

#排序
cars = ['bow','audi','toyota','subaru']
cars.sort()                                #永久排序
print(cars)
cars.sort(reverse = True)                  #反排序
print(cars)
print(sorted(cars))                        #临时排序
print(cars)

#倒序
cars.reverse()                             #只倒不排

#确定列表长度
len(cars)

#创建数字列表
for value in range(1,5) :                  #range()生成一系列数字，不包含最后一个
    print(value)
numbers = list(range(1,21,2))                 #把range()生成的数字转化成列表   2为步长
print(numbers)

squares = []
for value in range(1,11) :
    squares.append(value**2)
print(squares)

#数字列表的大小,求和
digits = [1,4,2,7,5,8,6,0,9]
print(min(digits))
print(max(digits))
print(sum(digits))

#列表解析
square = [value**2 for value in range(1,5)]
print(square)


#切片
players = ['charles','matina','michael','florence','eli']
print(players[1:3])                              #不包括3
print(players[:4])
print(players[1:])

#遍历切片
for player in players[0:3]:
    print(player)

#copy list
players_2 = players[:]                          #建立副本，两列表互不影响

"""
players_3 = players                             #这样不行，两者指向同一个列表

"""



#practice

"""

for number in range(1,21):
    print(number)

ran = list(range(1,21,2))
for rans in ran:
    print(rans)

sub = list(range(3,31,3))
print(sub)

li = [value**3 for value in range(1,11) ]
print(li)


print("\n.................\n")
place = ['pari','beijing','newyork','tokiyo','xini']
print(place)

print(sorted(place))
print(place)

place.sort(reverse=True)
print(place)

place.reverse()
print(place)

invite_namelist = []
invite_namelist.append('google')
invite_namelist.append('baidu')
invite_namelist.insert(1,'sogou')
invite_namelist.append('biying')
invite_namelist.insert(1,'sm')
print(invite_namelist)

unable = invite_namelist.pop(1)
print("The " + unable + " is unwilling to come !")
print("\n......................\n")

for name in invite_namelist :
    print('Hello ' + name + ', welcome to the party !')

print("\n...................\n")
i = len(invite_namelist)                #确定列表长度
sorry_name = []
while i > 2 :
    sorry_name.append(invite_namelist.pop())
    i = i - 1
for name in sorry_name :
     print(name + " ,I am sorry that you can't come to the party!")

for name in invite_namelist :
    print(name + " ,You are still in the invited namelist !")

del invite_namelist[0]
del invite_namelist[0]
print(invite_namelist)
 
"""