#1. loop
#a. loop of 'for'
# 遍历数字范围（0-4）
a = 5
for i in range(a):
    print(i)  # 输出>=0且<a的整数

# 遍历列表
animals = ["猫", "老虎", "鳄鱼"]
for animal in animals:
    print(f"我喜欢养{animal}")  # 格式化字符串，更简洁的拼接方式。输出“我喜欢养猫，我喜欢养老虎，我喜欢养鳄鱼”
print(f"我喜欢养{animals}")# 输出：“我喜欢养['猫', '老虎', '鳄鱼']”

#b. loop of 'while'
# 计算100以内正整数奇数的和(make by myself)
a = -1
b = 0
while a + 2 < 100:
    a = a + 2
    b = a + b
print(b)
# 计算100以内正整数奇数的和（make by Ai）
a = 1  # a：当前遍历的奇数（从第一个正奇数1开始，而非-1）
b = 0  # b：存储奇数的累加和
while a < 100:
    b += a  # 等价于b = b + a，累加当前奇数到总和中
    a += 2  # 切换到下一个奇数（步长2）
print("100以内奇数的和为：", b)  # 输出结果：2500

#2. list
# 创建列表
numbers = [1, 2, 3, 4, 5]
mixed = [1, "苹果", 3.14, True]  # 可以存储不同类型的数据

# 访问列表元素（索引从0开始）
print(numbers[0])  # 第一个元素：1
print(numbers[-1]) # 最后一个元素：5

# 修改元素
mixed[1] = False
numbers[2] = 30
print(numbers)     # 输出：[1, 2, 30, 4, 5]
print(mixed)
# 列表常用操作
numbers.append(6)  # 添加元素到末尾：[1,2,30,4,5,6]
numbers.remove(2)  # 删除指定元素：[1,30,4,5,6]
print(len(numbers))# 列表长度：5

#3. function
# 定义函数：计算两个数的和
def add(a, b):
    """这是一个加法函数，返回a+b的结果"""  # 函数说明文档
    result = a + b
    return result  # 返回结果

# 调用函数
sum1 = add(10, 20)
print(sum1)  # 输出：30

sum2 = add(5.5, 4.5)
print(sum2)  # 输出：10.0

#练习（计算器）
def calculator():
    print("===== 简易计算器 =====")
    # 获取用户输入的两个数字
    try:
        num1 = float(input("请输入第一个数字："))
        num2 = float(input("请输入第二个数字："))
    except ValueError:
        print("输入错误！请输入有效的数字。")
        return

    # 选择运算类型
    print("\n请选择运算类型：")
    print("1. 加法 (+)")
    print("2. 减法 (-)")
    print("3. 乘法 (*)")
    print("4. 除法 (/)")

    choice = input("请输入选项（1/2/3/4）：")

    # 根据选择计算并输出结果
    if choice == "1":
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif choice == "2":
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif choice == "3":
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif choice == "4":
        if num2 == 0:
            print("错误！除数不能为0。")
        else:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
    else:
        print("输入错误！请选择1-4的选项。")
# 调用计算器函数
calculator()
#核心新知识点：while True 无限循环、break（终止循环）、continue（跳过本次循环）；
a = 34.1125
while True:
    a += 2
    if a > 100 :
        break
print(a)

#4. simple type of data
'''
int（整数）
float（浮点数）存数值
str（字符串）存文本
bool（布尔值）存真假
list（列表，可修改）
tuple（元组，不可修改）存多个数据
dict（字典）以键值对形式存数据。
'''

#5. tuple
# a. 定义元组
point = (10, 20)          # 普通元组（坐标）
single = (5,)             # 单个元素的元组（必须加逗号）
mix_tuple = (1, "apple", 3.14)  # 混合类型元素

# b. 取值（唯一核心操作，因为不能修改）
print(point[0])           # 取第一个元素，输出 10
print(mix_tuple[1:3])     # 切片，输出 ('apple', 3.14)

# c. 尝试修改会报错（验证不可修改特性）
# point[0] = 15  # 执行这行会报 TypeError: 'tuple' object does not support item assignment

# d. 常用场景：函数返回多个值（本质是元组）
def a():
    return 100, 200  # 等价于 return (100, 200)
width, height = a()
print(width, height)  # 输出 100 200

#6. dict
# a. 定义字典
person = {
    "name": "小明",
    "hobbies": ["打球", "听歌"]  # 值可以是列表
}

# 2. 取值（核心操作：通过键取值）
print(person["name"])       # 如果没有name，会KeyError报错
print(person.get("age"))    # 如果没有age，会输出none