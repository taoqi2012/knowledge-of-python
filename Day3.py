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