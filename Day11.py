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

# 场景 3：匹配列表 / 元组的结构（最实用的场景）
# match-case 能匹配容器的长度、元素值、甚至通配元素，适合解析固定结构的序列：
# 示例1：匹配列表的固定结构
def parse_list(lst):
    match lst:
        case [1, 2, x]:  # 匹配长度为3、前两个元素是1和2的列表，第三个元素绑定到x
            print(f"匹配成功！第三个元素是：{x}")
        case [a, b, c, d]:  # 匹配长度为4的列表，元素分别绑定到a/b/c/d
            print(f"4元素列表：{a}+{b}+{c}+{d}={a+b+c+d}")
        case [*rest]:  # *rest 匹配任意长度的列表，rest绑定所有元素（通配）
            print(f"其他列表，元素：{rest}")

# 测试
parse_list([1,2,5])    # 输出：匹配成功！第三个元素是：5
parse_list([1,2,3,4])  # 输出：4元素列表：1+2+3+4=10
parse_list([10,20])    # 输出：其他列表，元素：[10,20]

# 示例2：匹配元组（和列表逻辑一致）
def parse_tuple(t):
    match t:
        case ("姓名", name):  # 匹配第一个元素是"姓名"的二元组，第二个元素绑定到name
            print(f"姓名：{name}")
        case ("年龄", age):
            print(f"年龄：{age}岁")
        case _:
            print("无效元组")

parse_tuple(("姓名", "张三"))  # 输出：姓名：张三
parse_tuple(("年龄", 20))      # 输出：年龄：20岁

# 场景 4：匹配字典（简易版）
# 匹配字典的指定键值对（注：match-case 匹配字典时，默认只检查「指定的键是否存在且值匹配」，不要求完全匹配）：
def parse_dict(d):
    match d:
        case {"name": name, "age": age}:  # 匹配包含name和age键的字典
            print(f"姓名：{name}，年龄：{age}")
        case {"type": "fruit", "name": fruit}:  # 匹配type=fruit的字典
            print(f"水果：{fruit}")
        case _:
            print("无效字典")

# 测试
parse_dict({"name": "李四", "age": 25})          # 输出：姓名：李四，年龄：25
parse_dict({"type": "fruit", "name": "苹果"})    # 输出：水果：苹果
parse_dict({"score": 90})                       # 输出：无效字典

# 练习 2：解析用户指令（匹配列表结构）
# 要求
# 用户输入指令是列表格式，如 ["添加", "商品", "苹果"]、["删除", "订单", 1001]；
# 用 match-case 匹配指令结构，执行对应操作：
# 匹配 ["添加", "商品", 商品名]：打印「添加商品：xxx」；
# 匹配 ["删除", "订单", 订单号]：打印「删除订单：xxx」；
# 其他指令：打印「无效指令」。
def order(a):
    match a:
        case ["添加","商品",x]:
            print(f"添加商品{x}")
        case ["删除", "订单", y]:
            print(f"删除订单{y}")
        case _:
            print("无效指令")

order(["添加","商品","巧克力"])