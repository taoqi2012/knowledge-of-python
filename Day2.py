#1. loop
#a. loop of 'for'
# 遍历数字范围（0-4）
# a.range(起始值)
# 生成 0 到 4 的整数序列（不包含 5）
nums = range(5)
# 转成列表查看具体元素（方便理解，实际循环中无需转换）
print(list(nums))  # 输出：[0, 1, 2, 3, 4]
# 常用场景：控制循环执行 5 次
for i in range(5):
    print(f"循环第 {i+1} 次，i的值：{i}")
# 输出：
# 循环第 1 次，i的值：0
# 循环第 2 次，i的值：1
# 循环第 3 次，i的值：2
# 循环第 4 次，i的值：3
# 循环第 5 次，i的值：4

# b.range(起始值，终止值)
# 生成 1 到 10 的整数序列（不包含 11）
nums = range(1, 11)
print(list(nums))  # 输出：[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 常用场景：遍历 1-5 的数字
for num in range(1, 6):
    print(f"当前数字：{num}")
# 输出：
# 当前数字：1
# 当前数字：2
# 当前数字：3
# 当前数字：4
# 当前数字：5

# c.range(起始值，终止值，步长)
# 生成 0, 2, 4, 6, 8（从0开始，步长2，到10结束）
nums1 = range(0, 10, 2)
print(list(nums1))  # 输出：[0, 2, 4, 6, 8]

# 生成 1, 4, 7（从1开始，步长3，到10结束）
nums2 = range(1, 10, 3)
print(list(nums2))  # 输出：[1, 4, 7]# 生成 10, 8, 6, 4, 2（从10开始，步长-2，到0结束）
nums3 = range(10, 0, -2)
print(list(nums3))  # 输出：[10, 8, 6, 4, 2]

# 生成 5, 4, 3, 2, 1（从5开始，步长-1，到0结束）
nums4 = range(5, 0, -1)
print(list(nums4))  # 输出：[5, 4, 3, 2, 1]

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

# 访问列表元素
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 基础切片：取 2-5（不包含5）
print(nums[2:5])  # [2, 3, 4]

# 省略 start：从开头取到 5（不包含）
print(nums[:5])   # [0, 1, 2, 3, 4]

# 省略 stop：从 5 取到末尾
print(nums[5:])   # [5, 6, 7, 8, 9]

# 步长 2：每隔1个取一个
print(nums[::2])  # [0, 2, 4, 6, 8]

# 负步长：倒序取值
print(nums[::-1]) # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# 切片赋值（批量修改）
nums[0:3] = [10, 20, 30]  # 将前3个元素替换为 10,20,30
print(nums)  # [10, 20, 30, 3, 4, 5, 6, 7, 8, 9]

# 修改元素
mixed[1] = False
numbers[2] = 30
print(numbers)     # 输出：[1, 2, 30, 4, 5]
print(mixed)

# 列表常用操作
# 添加：
fruits = ["苹果", "香蕉", "橙子"]

# append：末尾加单个元素
fruits.append("葡萄")
print(fruits)  # ['苹果', '香蕉', '橙子', '葡萄']

# extend：批量加元素（注意：参数必须是可迭代对象，如列表、字符串）
fruits.extend(["草莓", "西瓜"])
# 错误示例：fruits.extend("荔枝") → 会拆分成 ['荔','枝'] 插入，需用 fruits.extend(["荔枝"])
print(fruits)  # ['苹果', '香蕉', '橙子', '葡萄', '草莓', '西瓜']

# insert：指定位置插入
fruits.insert(0, "榴莲")  # 在索引0（第一个位置）插入
print(fruits)  # ['榴莲', '苹果', '香蕉', '橙子', '葡萄', '草莓', '西瓜']

fruits = ["榴莲", "苹果", "香蕉", "香蕉", "橙子"]

# 删除：
# del：按索引删
del fruits[0]
print(fruits)  # ['苹果', '香蕉', '香蕉', '橙子']

# remove：按值删（只删第一个匹配项）
fruits.remove("香蕉")
print(fruits)  # ['苹果', '香蕉', '橙子']

# pop：删元素并返回（常用在需要用到删除值的场景）
last_fruit = fruits.pop()
print(last_fruit)  # 橙子
print(fruits)      # ['苹果', '香蕉']

# clear：清空
fruits.clear()
print(fruits)      # []

#列表的常用内置方法（高频）
nums = [1, 2, 3, 2, 4, 2]
print(nums.index(2))  # 1（第一个2的索引）
print(nums.count(2))  # 3（2出现3次）
nums = [3, 1, 4, 2, 5]

# sort：原地升序
nums.sort()
print(nums)  # [1, 2, 3, 4, 5]

# sort：原地降序
nums.sort(reverse=True)
print(nums)  # [5, 4, 3, 2, 1]

# sorted：生成新列表（原列表不变）
new_nums = sorted(nums)
print(new_nums)  # [1, 2, 3, 4, 5]
print(nums)      # [5, 4, 3, 2, 1]

# reverse：原地反转
nums.reverse()
print(nums)      # [1, 2, 3, 4, 5]
fruits = ["苹果", "香蕉", "橙子"]
print(len(fruits))       # 3（长度）
print("香蕉" in fruits)  # True（存在）
print("榴莲" not in fruits)  # True（不存在）

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