# 毕向东视频笔记  
-----------------------

## Day 7 

### 06  子父类中构建器的特点  

每个子类构建器的第一行为隐式表达式super();  
即默认调用父类的默认构建器进行初始化  
如果父类没有空参数的构建器，则需要在子类构建器用super()语句进行显式初始化(手动初始化)super(4);   
如果子类构建器的第一行需要调用自身的其他构建器，为this();则没有super();

##### 子类访问父类构建器的原因：  
子类可以直接获取父类中的数据，所以需要查看父类是如何对这些数据进行初始化的  

### 07 Final关键字  

final修饰符可以修饰类，函数，变量  
1. 被final修饰的类不可以被继承,为了避免被继承，被子类复写功能    
	> 保证封装性  
- 被final修饰的方法不能被复写  
- 被final修饰的变量是一个常量只能赋值一次，既可以修饰成员变量，也可以修饰局部变量  
	> 常量书写规范：所有字母大写，如果含有多个单词，单词间通过_连接  
- 内部类定义在类中的局部位置上时，只能访问该局部被final修饰的局部变量  
 
##### 语法：  

```java
final class Person {
	void show() {}
	final int speak() {}
	public static final MY_PI = 3.1415926;
}
```
### 08-09 抽象类  

当多个类中出想相同功能，但是功能的主体不同时，可以向上抽取，只抽取功能的定义，需求，或部分相同功能，而不抽取功能的主体，建立抽象类。  

1. 抽象方法一定要放在抽象类中  
- 抽象方法和抽象类必须被abstract关键字修饰  
- 抽象类不可以用new创建对象，因为调用对象没意义  
- 抽象类中的方法要被使用，必须由子类复写所有的抽象方法后，建立子类对象使用  
	> 如果子类只复写了部分抽象方法，那么该子类还是一个抽象类  
- 抽象类可以不定义抽象方法，而只用于控制不能建立该类对象  

```java
//抽象类
abstract class Student {
	//该方法没有主体
    abstract void study();
}

class BaseStudent extends Student {
	//子类复写抽象类的抽象方法  
    void study() {
        System.out.println("Base Study");
    }
}

class AdvAtudent extends Student {
    void study() {
        System.out.println("Advance Study");
    }
}
```

### 11 模板方法模式  

定义功能时，功能的一部分是确定的，且确定的部分包含在不确定的部分中，那么就将不确定的部分暴露出去，由该类的子类去继承  

```java
abstract class GetTime {
    public final void getTime() {
        long start = System.currentTimeMillis();
		//模板	
        runcode();
        long end = System.currentTimeMillis();
        System.out.println("毫秒：" + (end-start));
    }
    public abstract void runcode();
}

//重写模板
class SubTime extends GetTime {
    public void runcode() {
        for (int x = 0; x < 100; x++) {
            System.out.println(x);
        }
    }
}

public class TemplateDemo {
    public static void main(String[] args) {
        SubTime time = new SubTime();
        time.getTime();
    }
}
```

### 12-14 接口  

##### 当抽象类中的方法都是抽象的，那么可以通过接口的形式来表示  

1. class 用于定义类，interface 用于定义接口  
- implements关键字用于实现接口  
- 接口可以被类多实现（一个类可以实现多个接口）  
- 接口中定义的常量可以直接调用  
- 一个类可以继承的同时可以多实现  
- 接口间可以相互继承  
- 接口间可以多继承  

**格式特点：**  
1. 接口中常见定义：常量，抽象方法  
2. 接口成员有固定修饰符  
	- 常量：public static final  
	- 方法：public abstract   
3. 修饰符可以省略，编译器自动加，**但是建议写全**  

```java
//定义接口 
interface Inter {
    public static final int NUN = 3;
    public abstract void show();
}

interface InterA {
    public abstract void method();
}

//用implements实现接口  
class Test implements Inter,IntetA {
    public void show() {
        System.out.println("show");
    }
	public void method(){}
}

public class InterfaceDemo {
    public static void main(String[] args) {
        Test test = new Test();
        System.out.println(test.NUN);
        System.out.println(Test.NUN);
        System.out.println(Inter.NUN);
    }
}

```  

## Day 8  

### 01-02 多态  

事物存在的多种形态  

##### 1. 多态的体现  
    - 父类的引用也可以接受子类对象    
##### 2. 多态的前提  
	- 类与类之前必须有关系，要么继承，要么实现  
	- 存在重写  
##### 3. 多态的好处  
	- 大大提高了程序的拓展性  
##### 4. 多态的局限  
	- 只能使用父类的引用访问父类中的成员    

```java
abstract class Animal {
    abstract void eat();
}

class Cat extends Animal {
    void eat() {
        System.out.println("吃鱼");
    }
    void CatchMouse() {
        System.out.println("抓老鼠");
    }
}

class Dog extends Animal {
    void eat() {
        System.out.println("吃肉");
    }
    void bark() {
        System.out.println("叫");
    }
}

class Pig extends Animal {
    void eat() {
        System.out.println("吃草");
    }
    void gongDi() {
        System.out.println("拱地");
    }
}

public class DuoTaiDemo {
    public static void main(String[] args) {
        Cat cat = new Cat();
        Dog dog = new Dog();
        Animal pig = new Pig();
        cat.CatchMouse();
        function(cat);
        function(dog);
        function(pig);
    }
    public static void function (Animal animal) {
        animal.eat();
    }
}

```

### 03 转型  

1. 不能将父类对象转换为子类类型  
- 将父类引用指向自己的子类对象时，该引用可以被提升，也可以被强制转换  
- 多态自始自终是子类对象的变化  
- instancdof关键词判断是那个子类引用  
	- 子类型有限  
	- 需要对子类型进行其他操作  

```java  
public class DuoTaiDemo2 {
    public static void main(String[] args) {
        Animal a = new Cat();
        a.eat();
        fuc(a);
        fuc(new Dog());
    }
    public static void fuc(Animal animal) {
        if (animal instanceof Cat) {
            Cat c = (Cat)animal;
            c.CatchMouse();
        }
        else if (animal instanceof Dog) {
            Dog d = (Dog)animal;
            d.bark();
        }
    }
```

### 04-05 多态中成员的特点  
非静态  
在编译期：参阅引用型变量(句柄类)所属的类中是否含有调用的方法，如果有，编译通过，否则失败  
在运行期：参阅对象所属的类中是否含有调用的方法  
引用型变量 a = new 对象所属的类  

对于静态方法  
无论编译还是运行期，都参考（引用型变量所属的类）  

在多态中，成员变量的特点  
无论在编译和运行期，都参考（引用型变量所属的类）  

### 06-07 多态的主板实例  

```java
interface PCI {
    public abstract void open();
    public abstract void close();
}

class MainBoard {
    public void run() {
        System.out.println("MainBoard Run");
    }

    public void runPCI(PCI pci) {
        pci.open();
        pci.close();
    }
}

class NetCard implements PCI {
    public void open() {
        System.out.println("NetCard Open");
    }

    public void close() {
        System.out.println("NetCard Close");
    }
}

class SoundCard implements PCI {
    public void open() {
        System.out.println("SoundCard Open");
    }

    public void close() {
        System.out.println("SoundCard Close");
    }

}

public class DuoTaiDemo5 {
    public static void main(String[] args) {
        MainBoard mainBoard = new MainBoard();
        mainBoard.run();
        mainBoard.runPCI(new NetCard());
        mainBoard.runPCI(new SoundCard());
    }
}
```











 
