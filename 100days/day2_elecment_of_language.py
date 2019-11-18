a = 321
b = 123
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b) # 求模
print(a % b)  #求余数
print(a ** b)



#type()用来检查变量类型
a = 100 
b = 12.345
c = 1 + 5j  #复数
d = 'hello world'
e = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
"""
int()：将一个数值或字符串转换成整数，可以指定进制。
float()：将一个字符串转换成浮点数。
str()：将指定的对象转换成字符串形式，可以指定编码。
chr()：将整数转换成该编码对应的字符串（一个字符）。
ord()：将字符串（一个字符）转换成对应的编码（整数）。
"""

"""
使用input()函数获取键盘输入(字符串)
使用int()函数将输入的字符串转换成整数
使用print()函数输出带占位符的字符串
上面的print函数中输出的字符串使用了占位符语法，
其中%d是整数的占位符，%f是小数的占位符，%%表示百分号
"""

a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %f' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))

"""
运算符
 []下标,[:]切片
** 指数
~ 按位取反,+-正负号
* 乘 / 除 % 模 // 整除
+-加减
>> << 右移 左移
& 与
^ | 异或 或
<= < > >= 
== != 
is is not 
in not in 
not or and 
= += -= *= /= %= //= **= &= `
"""
#计算园的周长和面积
import math

radius = float(input("请输入圆半径: "))
perimeter = 2 * math.pi * radius 
area = math.pi * radius * radius 
print("周长:%.2f"% perimeter)
print('面积: %.2f'% area)


year = int(input("请输入年份:"))
is_leap = (year % 4 == 0 and year % 100 != 0) or \
        year % 400 == 0
print(is_leap)












