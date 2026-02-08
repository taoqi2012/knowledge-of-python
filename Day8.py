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
        print(f"打印姓名：{self.name}，年龄：{self.age}",end = " ")

class Teacher(Person):
    def __init__(self,name,age,subject):
        super().__init__(name,age)
        self.subject = subject
    def show_teacher_info(self):
        super().show_base_info()
        print(f"教科目：{self.subject}")

b = Teacher("陶老师",25,"语文")
b.show_teacher_info()



# 预设起始单词（如 "apple"），提示用户输入下一个单词；
# 规则：新单词的首字母必须等于上一个单词的尾字母（如 apple 尾字母是 e，下一个可以是 egg）；
# 用 while 循环实现，直到用户输入错误为止，打印「接龙失败」。
def word_chain(first_word):
    a = [first_word]
    while True:
        new_word = input(f"当前单词为{first_word},请输入接龙的单词:")
        if new_word in a:
            print("接龙失败，游戏结束")
            break
        elif first_word[-1] == new_word[0]:
            print(f"接龙成功！当前单词更新为：{new_word}")
            first_word = new_word
            a.append(new_word)
        else:
            print("接龙失败，游戏结束")
            break

word_chain("banana")