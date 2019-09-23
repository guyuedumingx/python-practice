"""

学习if语句和字典和集合
wang daka

!= 不相等
== 相等

and
or

"""
car = 'subaru'
print("\nIs car = 'subaru'? I predict True")
print(car == 'subaru')
print("\nIs car = 'audi'? I predict False")
print(car == 'audi')

#检查特定值是否在列表中
banned_users = ['andrew','carolina','david']
user_1 = 'marie'
user_2 = 'andrew'

if user_1 not in banned_users :
    print("\n" + user_1.title() + ", you can post a response if you wish.")

if user_2 in banned_users :
    print(user_2.title() + ", you are benned!")


#if-elif-else 语句
age = 19
if age >= 18 :
    print("You are an adoult!")
else:
    print("You are a teen")

#确定列表非空
re = []
if re :                              #re = False
    print("not")
else :
    print('yes')
print("\n..................\n")

#使用多个列表
available_toppings = ['mushrooms','olives','green peppers',
                       'pepperoni','pineapple','extra cheese']
request_toppings = ['mushrooms','fresh fries','extra cheese']

for request_topping in request_toppings:
    if request_topping in available_toppings:
        print("The " + request_topping + ", has reading")
    else:
        print("Sorry, We don't have " + request_topping)
print("\nFinish making you pizza!")


#字典
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print("You has earned " + str(new_points) + ' points !')

#添加键对值
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#修改字典中的值
alien_0['color'] = 'yellow'
print(alien_0['color'])

#删除字典中的键值对
del alien_0['points']
print(alien_0)


information = {
        'first_name':'wang',
        'last_name':'daka',
        'adress':'guangdong',
        'age':'20',
        'full_name':'wang',
        }
print(information)


#遍历所有的键值对
for key,value in information.items():
    print("\nKEY: " + key.title())
    print("VALUE： " + value.title())

print("\n..................\n")

#遍历所有的键
for key in information.keys():
    print(key)


#遍历所有的值
for value in information.values():      #不考虑重复
    print(value)


#按顺序遍历所有的键
for key in sorted(information.keys()):
    print(key.title())

#集合可除去列表中的重复项
for name in set(information.values()):
    print(name.title())

#嵌套（将一系列字典储存在列表中或将列表作为值存储在字典中）
"""
alien_1 = {'color':'green','points':5}
alien_2 = {'color':'green','points':10}
alien_3 = {'color':'green','points':15}

aliens = [alien_1,alien_2,alien_3]             #将字典存储在列表中

for alien in aliens:
    print(alien)
"""

aliens = []

#创建30个外星人
for alien_number in range(30):              
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print('\n................')


#在字典中储存列表
pizza = {
    'crust':'thick',
    'toppings': ['mushrooms','extra cheese'],
}
print("You ordered a " + pizza['crust'] + " -crust pizza" + 
        " with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)


#在字典中存储字典
users = {
    'wang':{
        'first':'albert',
        'last':'harden',
        'age':'25',
    },
    'mcurie':{
        'first':'fasfv',
        'last':'asfvv',
        'age':'55',
    }
}
for username,user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + ' ' + user_info['last']   #引用方法
    age = user_info['age']

    print("\tFull name: " + full_name.title())
    print("\tage: " + age.title()) 


#practise