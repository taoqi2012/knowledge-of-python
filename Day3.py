#1. comparison operator（比较运算符）
# 错误示例
# # 想判断age是否等于18，却写成赋值
# if age = 18:  # 报错！SyntaxError
#     print("成年")
# 正确写法
age = 18
if age == 18:
    print("成年")  # 正常执行
# == vs is：值相等 ≠ 身份相等
a = [1,2,3]
b = [1,2,3]

print(a == b)  # True（值完全一样）
print(a is b)  # False（两个列表在内存中是不同对象）
c = a
print(a is c)  # True（c和a指向同一个列表对象）

# 比较数字
# 定义变量
num1 = 10
num2 = 5
num3 = 10
# 逐个测试
print(num1 == num3)  # True（值相等）
print(num1 != num2)  # True（值不等）
print(num1 > num2)   # True（10>5）
print(num1 < num2)   # False（10不小于5）
print(num1 >= num3)  # True（10>=10）
print(num2 <= num3)  # True（5<=10）

# 判断一个数是否是偶数
def numbers():
    number = int(input("请输入一个数，判断是否是偶数"))
    if number % 2 == 0:  # 余数等于0 → 偶数
        print(f"{number} 是偶数")
    else:
        print(f"{number} 是奇数")
numbers()

# 判断用户输入的密码长度是否在 8-20 位之间
def length():
    password = input("判断输入的密码长度是否在 8-20 位之间")
    numberlen = len(password)
    if 8 <= numberlen <= 20:
        print(f"{password}在 8-20 位之间")
    else:
        print(f"{password}不在8-20 位之间")
length()

# Python 三大逻辑运算符（全汇总）
#名称	作用
#and	所有条件都为 True，结果才为 True；有一个 False 则为 False
#or		只要有一个条件为 True，结果就为 True；全 False 才为 False
#not	对条件取反（True 变 False，False 变 True)
# 例子：
'''
A	    B	       A and B	   A or B	   not A
True	True	   True	       True	       False
True	False	   False	   True	       False
False	True	   False	   True	       True
False	False	   False	   False	   True
'''
# 1. and（逻辑与：全真才真）
# 需求：判断年龄是否在18-60岁之间（等价于 18<=age and age<=60）
age = 25
print(age >= 18 and age <= 60)  # True（两个条件都满足）

age = 17
print(age >= 18 and age <= 60)  # False（第一个条件不满足）

# 2. or（逻辑或：一真就真）
# 需求：判断是否是周末（周六 或 周日）
weekday = "周六"
print(weekday == "周六" or weekday == "周日")  # True（满足一个）

weekday = "周一"
print(weekday == "周六" or weekday == "周日")  # False（都不满足）

# 3. not（逻辑非：取反）
# 需求：判断是否不是偶数
number = 5
print(not (number % 2 == 0))  # True（5是奇数，对“是偶数”取反）

number = 4
print(not (number % 2 == 0))  # False（4是偶数，取反后为假）

# 4. 组合使用（多条件）
# 需求：判断是否是成年人且不是老年人（18<=age<60）
age = 50
print(age >= 18 and not (age >= 60))  # True

age = 65
print(age >= 18 and not (age >= 60))  # False

# 优先级（先算比较，再算逻辑）
# 运算优先级：() > not > and > or → 不确定就加括号，避免出错：

# 假值：0、""（空字符串）、[]（空列表）、None；
# 真值：非 0 数字、非空字符串 / 列表等。
print(0 and 10)  # 0（第一个是假值，直接返回0）
print("abc" or 0) # "abc"（第一个是真值，直接返回"abc"）
print(not "")     # True（空字符串是假，取反为真）


def check_password_strength():
    password = input("请输入密码：").strip()
    # 条件1：长度8-20位
    length_ok = 8 <= len(password) <= 20
    # 条件2：包含数字（遍历密码，判断是否有字符是数字）
    has_number = any(char.isdigit() for char in password)

    # 逻辑与：两个条件都满足才合格
    if length_ok and has_number:
        print(f"密码「{password}」强度合格")
    else:
        # 提示具体哪里不合格
        if not length_ok:
            print("密码长度必须在8-20位之间")
        if not has_number:
            print("密码必须包含数字")
check_password_strength()