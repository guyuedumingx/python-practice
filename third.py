"""
学习元组
wang daka

不能修改元组的数据
"""

dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

#修改元组的变量
dimensions = (300,100)         #允许重新赋元组
print(dimensions)

i = 4
dimen = (i,2)
print(dimen[0])
i = 5
print(dimen[0])                #不接受i的新值
