# 一、match-case 是什么？（核心概念）
# match-case 是 Python 的模式匹配语句，可以理解为「增强版的 if-elif-else」，但功能更强大：
# 它能匹配值、数据类型、列表 / 元组 / 字典结构、甚至类实例；
# 语法更简洁，逻辑更清晰，尤其适合多分支、多结构的判断场景。

# 基础语法
# match 要匹配的变量/表达式:
#     case 模式1:
#         执行代码1
#     case 模式2:
#         执行代码2
#     case _:  # 通配符，匹配所有未命中的情况（类似else）
#         执行默认代码

# 二、基础用法（从简单到复杂）
# 场景 1：匹配固定值（替代简单的 if-elif）
# 最基础的用法：匹配变量的具体值，替代 if x == 1: ... elif x == 2: ...

# 示例：根据数字返回对应星期
def get_weekday(num):
    match num:
        case 1:
            return "星期一"
        case 2:
            return "星期二"
        case 3 | 4 | 5:  # 多值匹配（| 表示或）
            return "周三到周五"
        case 6 | 7:
            return "周末"
        case _:  # 通配符，匹配所有其他情况
            return "无效数字（请输入1-7）"

# 测试
print(get_weekday(3))  # 输出：周三到周五
print(get_weekday(6))  # 输出：周末
print(get_weekday(8))  # 输出：无效数字（请输入1-7）


# 练习 1：简易计算器（用 match-case 替代 if-elif）
def calculator(num1, op, num2):
    match op:
        case "+":
            print(num1 + num2)
        case "-":
            print(num1 - num2)
        case "*":
            print(num1 * num2)
        case "/":
            print(num1 / num2)


calculator(45, "/", 9)

# 场景 2：匹配数据类型（替代 type () 判断）
# 可以直接匹配变量的类型，比 if type(x) == int: ... 更简洁：

# 示例：根据输入类型做不同处理
def process_input(x):
    match x:
        case int():
            print(f"你输入的是整数：{x}，翻倍后：{x*2}")
        case str():
            print(f"你输入的是字符串：{x}，大写后：{x.upper()}")
        case list():
            print(f"你输入的是列表：{x}，长度：{len(x)}")
        case _:
            print(f"不支持的类型：{type(x)}")

# 测试
process_input(10)       # 输出：你输入的是整数：10，翻倍后：20
process_input("hello")  # 输出：你输入的是字符串：hello，大写后：HELLO
process_input([1,2,3])  # 输出：你输入的是列表：[1,2,3]，长度：3