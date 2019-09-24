"""
学习读取文件
学习异常
wang daka
"""


#读取整个文件
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)


#逐行读取
filename = 'pi_digits.txt'
with open(filename) as file:
    for line in file:
        print(line.rstrip())


#创建一个包含文件各行内容的列表
file_name = 'pi_digits.txt'
with open(file_name) as fileobject:
    lines = fileobject.readlines()    #读取每一行，并把它保存在列表中

for line in lines:
    print(line.rstrip())


#写入文件
"""
'r'读取模式
'w'写入模式
'a'附加模式
'r+'读取与写入
Python只能写入字符串
"""

#写入多行
name = 'programming.txt'
with open(name,'w') as object:              #没有的会自己生成该文件,覆盖文件内容
    object.write("I love programming!\n")
    object.write("I love creating new games!")


#附加到文件
with open(name,'a') as ob:
    ob.write("I am a boy!\n")


#异常

print("You can enter q to exit")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break

    try:
        answer = int(first_number) / int(second_number)      #验证的步骤
    except ZeroDivisionError:               #报错时的操作
        print("You can't divide by zero!")
    else:                                   #正常情况下的操作
        print("\n" + answer)


#处理FileNotFoundError异常

open_file = 'alice.txt'


try:
    with open(open_file) as f_oj:
        content = f_oj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + open_file + ' does not exist.'
    print(msg)