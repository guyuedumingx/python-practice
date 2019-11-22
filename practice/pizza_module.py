"""
把函数封装在模块中
wang daka
"""


def make_pizza(size,*toppings):
    print("\nMaking a " + str(size) + 
    "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

def make_pizza_1(size,*toppings):
    print("\nMaking a " + str(size) + 
    "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)