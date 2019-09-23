"""

学习if语句和字典
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
for value in information.values():
    print(value)

