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



# 定义函数 sum_1_to_n(n)，接收一个正整数 n；
# 函数内计算 1+2+3+...+n 的累加和，返回结果；
# 调用函数，传入n=100，打印最终累加和；

# 1
def sum_1_to_n(n):
    a = 0
    b = 0
    while a + 1 <= n:
        a += 1
        b += a
    print(b)
sum_1_to_n(100)

# 2
def sum_2_to_n(n):
    a = 0
    for b in range(1,n+1):
        a += b
    print(a)
sum_2_to_n(100)



# 预设一个固定数字（比如secret_num = 7，作为秘密数字）；
# 用while循环实现：让用户不断输入数字，直到猜中预设数字为止；
# 添加简单提示：猜小了提示「猜小啦，再大一点」，猜大了提示「猜大啦，再小一点」，猜中了提示「恭喜！猜中了！」并终止循环；
def guess_num(x):
    a = int(input("你猜是什么数字:"))
    while a != x:
        if a < x:
            print("猜小啦，再大一点")
            a = int(input(""))
        elif a > x:
            print("猜大啦，再小一点")
            a = int(input(""))
    else:
        print("恭喜！猜中了！")
guess_num(94)



# 编写一个 Python 程序，实现以下功能：
# 接收用户输入的学生姓名和数学成绩（成绩为数字，可整数可浮点数）。
# 做前置判断：如果用户输入的成绩不是有效数字（提示：可先简单判断是否能转换为 float，或直接捕获异常），或者成绩小于 0 或大于 100，输出 「姓名」的成绩输入无效，请输入 0-100 之间的有效数字！。
# 有效成绩的判断规则：
# 成绩 大于等于 60：输出 「姓名」的数学成绩合格，继续加油！
# 成绩 小于 60（且不等于 0，特殊说明：0 分按 “缺考” 处理）：输出 「姓名」的数学成绩不合格，需要补考！
# 成绩 等于 0：输出 「姓名」缺考数学科目，请及时办理补考手续！
def information(name,grade):
    if float(grade) >= 60:
        print(f"{name}的成绩合格，继续加油！")
    elif float(grade) > 0:
        print(f"{name}的成绩不合格，需要补考！")
    else:
        print(f"{name}缺考，请及时办理补考手续！")
information("taoqi",3874338748348387483)