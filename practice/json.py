"""
learn json
save the user's information
wang daka
"""


import json

numbers = [2,3,5,7,11,13]

filename = 'numbers.json'
with open(filename,'w') as f_oj:
    json.dump(numbers,f_oj)        #将numbers写入f_oj

with open(filename) as file_object:
    number = json.load(file_object)  #读出file_object的数据

print(number)