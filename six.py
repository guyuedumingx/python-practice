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



