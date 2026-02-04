# 定义Student类，构造方法__init__接收 2 个参数：name（姓名）、score（成绩）。
# 定义 1 个实例方法show_info()，功能是打印学生信息，格式：姓名：XXX，成绩：XXX分。
# 实例化 1 个学生对象（比如姓名：张三，成绩：95），调用show_info()方法。
class Student:
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def show_info(self):
        print(f"姓名：{self.name}，成绩：{self.score}")
tq = Student("taoqi","80")
tq.show_info()

# 定义SimpleCalc类，构造方法__init__接收 2 个参数：a、b（两个要计算的数字）。
# 定义 1 个实例方法add()，功能是返回两个数字的和（无需打印，返回结果即可）。
# 实例化 1 个计算器对象（比如a=10，b=20），调用add()方法，打印最终的求和结果。
class SimpleCale:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        print(self.a + self.b)
example = SimpleCale(9,9812)
example.add()