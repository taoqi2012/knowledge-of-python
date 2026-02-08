# 定义Phone类，__init__接收 2 个参数：brand（品牌）、price（价格）；
# 定义实例方法show_info()，打印格式：品牌：XXX，价格：XXX元；
# 实例化 1 个手机对象（比如品牌：华为，价格：2999），调用show_info()。
class Phone:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price
    def show_info(self):
        print(f"品牌:{self.brand},价格：{self.price}")

huawei = Phone("华为",2999)
huawei.show_info()



# 定义Cup类，__init__接收 2 个参数：color（颜色）、capacity（容量，单位 ml）；
# 定义实例方法drink()，打印格式：我在用{color}的{capacity}ml水杯喝水；
# 实例化对象并调用drink()。
class Cup:
    def __init__(self,color,capacity):
        self.color = color
        self.capacity = capacity
    def drink(self):
        print(f"我在用{self.color}的{self.capacity}ml水杯喝水")

a = Cup("红色",1000)
a.drink()



# 定义父类Person：
# __init__接收name（姓名）、age（年龄）；
# 方法show_base_info()：打印姓名：XXX，年龄：XXX；
# 定义子类Teacher(Person)：
# __init__接收name、age、subject（教的科目）；
# 用super()调用父类__init__，绑定name和age；
# 定义方法show_teacher_info()：先调用父类show_base_info()，再打印教科目：XXX；
# 实例化Teacher对象（比如张三、30、数学），调用show_teacher_info()。
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show_base_info(self):
        print(f"打印姓名：{self.name}，年龄：{self.age}")

class Teacher(Person):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.subject = subject
    def show_teacher_info(self):
        super().show_base_info() and print(f"教科目：{self.subject}")

b = Teacher("陶老师",25,"语文")
b.show_teacher_info()