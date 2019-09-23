"""
学习类
wang daka

约定：大写字母名称指类
"""

class Dog():
    """模拟一只小狗"""
    def __init__(self,name,age):      #形参self必须在其他形参前面且必不可少
        """初始话属性name和age"""
        self.name = name              #以self为前缀的变量可以供类中所有方法使用
        self.age = age                #可以被实例引用 例：28行
        self.dog_type = 'tianyuanquan' #设置默认值

    def sit(self):
        """模拟小狗坐下"""
        print(self.name.title() + " is now sitting!")
    
    def roll_over(self):
        """模拟小狗打滚"""
        print(self.name.title() + " rolled over!")
    
    def change_type(self,type):
        self.dog_type = type


#根据类创建实例
my_dog = Dog('erha',2)

print("My dog's name is: " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")


my_dog.sit()
my_dog.roll_over()


#直接修改属性

my_dog.dog_type = 'jinmao'      
print(my_dog.dog_type)



#通过方法修改属性的值

my_dog.change_type('yidali')
print(my_dog.dog_type)


"""
继承
一个子类继承另一个父类的所有属性和方法
"""

class KittyDog(Dog):
    def __init__(self,name,age):
        """初始化父类的属性"""
        super().__init__(name,age)


your_dog = KittyDog('haha',1)
print(your_dog.name)