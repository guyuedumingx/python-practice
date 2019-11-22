"""
学习函数
wang daka
"""


#向函数传递一个参数
def greet_user(user_name):                #user_name是形参
    print("Hello " + user_name.title() + "!")

greet_user('wang')                        #wang是实参


#位置实参(按顺序给函数传递实参)
def describe_pet(animal_type,pet_name = 'erha'):         #pet_name默认为erha
    print("\nI have a " + animal_type)
    print("My " + animal_type + "'s name is " + pet_name)

describe_pet('dog','mimi')               #dog 对应着 animal_type
                                         #mimi 对应着 pet_name


#关键字实参
describe_pet(animal_type = 'hamster',pet_name = 'harry')    #无需知道位置，直接给形参赋值


#默认值
describe_pet('dog')

#practise



def make_shirt(site,type_word = 'I Love Python'):
    print("The T-shirt's site is: " + site + '.')
    print("The words you want to paint are: " + type_word)

make_shirt('long')
make_shirt(type_word='GOD',site = 'middle')


#返回值
#有默认值的参数必须放在无默认值参数后
def get_formatted_name(first_name,last_name,middle_name = ''):   #middle_name变为可选的
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name +' ' + last_name
    return full_name.title()                         #返回full_name

print(get_formatted_name('wang','daka','ww'))


#返回字典
def build_person(first_name,last_name,age=''):
    person = {'first':first_name,'last':last_name}
    if age:
        person['age'] = age

    return person

print(build_person('li','haha'))



#传递列表

def greet(names):
    for name in names:
        print("Hello " + name + "!")
    
users_name = ['wng','svasva','asrha','argggf']
greet(users_name)




#在函数中修改列表
#永久修改

greet_name = []

def greeting(names):
    while users_name:
        greet = (names.pop())
        print("Hello " + greet)
        greet_name.append(greet)

greeting(users_name)
print(len(users_name))

#禁止函数修改列表
def hello(names1):        
    while names1:
        names1.pop()

        
users_name2 = ['wng','svasva','asrha','argggf']

hello(users_name2[:])          #把副本传递给函数

#传递任意数量的实参
def pizza(*toppings):       #建立一个空元组存放实参
    print(toppings)

pizza('peperoni')
pizza('mushrooms','green peppers','extra cheese')


"""
如果要让函数接受不同类型的形参，
必须在函数定义中将接纳任意数量的形参放在最后
"""

#使用任意数量的关键字实参

def build_profile(first,last,**user_info):
    """创造一个字典，包含我们知道的用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

prompt = build_profile('wang','daka',age = '25',location = 'zhanjiang')
#键无需引号
print(prompt)


#导入模块
import pizza_module as pm       #用as指定别名
  
pm.make_pizza(16,'haha','egaeg','qethb','qqqevq')



#导入特定函数
"""
from module_name import function_name_1, fuction_name_2
from module_name import *  导入模块中的所有函数
"""
from pizza_module import make_pizza_1

make_pizza_1(11,'sdb','agaega','aggeq')           #无需使用句点表示


