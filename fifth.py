"""
学习用户输入以及while循环
wang daka
"""

#输入
prompt = "If you tell us who you are ,we can personalize the messages you see."
prompt += "\nWhat is your name: "                 #加本身


#让用户何时退出
#使用标志(active)
active = True
message = ''
while active :
    if message == 'quit':
        active = False
    else:
        message = input(prompt)
        print("\nHello, " + message.rstrip() + " !")
        print("你可以输入quit来退出!\n")


#使用break来退出循环
while True :
    city = input("Tell me the city: ")

    if city == 'quit':
        break
    else:
        print("I'm love to go to " + city.title() + "!\n")

