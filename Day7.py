# 定义一个函数 filter_even_numbers(num_list)，接收一个整数列表参数 num_list；
# 函数内实现功能：筛选出列表中所有的偶数（能被 2 整除的数，判断条件：num % 2 == 0）；
# 用for循环实现遍历和筛选，将筛选出的偶数存入一个新列表；
# 函数返回这个新的偶数列表，调用函数并打印结果；
def filter_even_numbers(num_list):
    list = []
    for a in num_list:
        if a % 2 == 0:
            list.append(a)
    print(list)
filter_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])



# 类 = 把「数据」和「操作数据的方法」打包在一起。

# 最基础的类结构（必须背下来）
# class 类名:
#     # 1. 初始化方法（构造方法）
#     def __init__(self, 参数1, 参数2):
#         self.属性1 = 参数1
#         self.属性2 = 参数2
#
#     # 2. 实例方法
#     def 方法名(self):
#         使用 self.属性 做事情

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def show(self):
        print(f"姓名：{self.name}，成绩：{self.score}")
s = Student("taoqi", 80)
s.show()



# 不想让外部随便改属性，就用双下划线变成私有。
class Student:
    def __init__(self, name, score):
        self.name = name
        self.__score = score



# 子类继承父类，拥有父类所有属性和方法，还能扩展。
# 基本结构
# class 父类:
#     ...
#
# class 子类(父类):
#     def __init__(self, 参数):
#         super().__init__(父类需要的参数)
#         # 子类自己的属性

# 练习
class Score:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def show(self):
        print(f"姓名：{self.name}，成绩：{self.score}")

class Analysis(Score):
    def __init__(self,name,score,last_score):
        super().__init__(name,score)
        self.last_grade = last_score
    def grade_analysis(self):
        if self.score >= self.last_grade:
            print(f"{self.name}考得不错，继续努力")
        else:
            print(f"{self.name}考得一般，得加油了")

t = Analysis("taoqi",80,75)
t.grade_analysis()