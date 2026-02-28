# 题目 1：基础闭包（计算累加和）
# 需求：
# 定义一个外部函数 counter()，内部定义一个变量 total = 0（用于存储累加和）；
# 定义内部函数 add(num)，功能是：
# 将传入的 num 加到 total 上；
# 返回更新后的 total；
# 外部函数返回内部函数 add；
# 编写测试代码：
# 创建闭包实例 my_counter = counter()；
# 依次调用 my_counter(1)、my_counter(2)、my_counter(3)，打印每次调用的返回值（预期输出：1、3、6）。
def counter():
    total = 0
    def add(num):
        nonlocal total
        total += num
        return total
    return add

my_counter = counter()
print(my_counter(1))
print(my_counter(2))
print(my_counter(3))



# 题目 2：进阶闭包（带初始值的乘法器）
# 需求：
# 定义外部函数 multiplier(base)，接收一个初始基数 base；
# 定义内部函数 multiply(num)，功能是返回 base * num；
# 外部函数返回内部函数 multiply；
# 编写测试代码：
# 创建两个闭包实例：
# double = multiplier(2)（基数为 2，实现 “翻倍” 功能）；
# triple = multiplier(3)（基数为 3，实现 “三倍” 功能）；
# 调用 double(5)、triple(5)，打印结果（预期输出：10、15）；
# 调用 double(10)、triple(10)，打印结果（预期输出：20、30）。
def multiplier(base):
    def multiply(num):
        nonlocal base
        return base * num
    return multiply

double = multiplier(2)
triple = multiplier(3)
print(double(5))
print(triple(5))
print(double(10))
print(triple(10))



# 题目 3：综合闭包（记录函数调用次数）
# 需求：
# 定义一个闭包函数 count_calls(func)，接收一个普通函数 func 作为参数；
# 内部定义一个变量 call_times = 0（记录被装饰函数的调用次数）；
# 定义内部函数 wrapper(*args, **kwargs)，功能是：
# 将 call_times 加 1；
# 打印 f"函数 {func.__name__} 已调用 {call_times} 次"；
# 调用传入的 func 并返回其结果；
# 外部函数返回内部函数 wrapper；
# 编写测试代码：
# 定义一个普通函数 add(a, b)，返回 a + b；
# 用闭包装饰 add：counted_add = count_calls(add)；
# 依次调用 counted_add(1,2)、counted_add(3,4)，打印每次的返回值和调用次数提示,预期输出：
# 函数 add 已调用 1 次
# 3
# 函数 add 已调用 2 次
# 7
def count_calls(func):
    call_times = 0
    def wrapper(*args):
        nonlocal call_times
        call_times += 1
        print(f"函数 {func} 已调用 {call_times}")
        return func(*args)
    return wrapper

def add(a,b):
    return a + b

counted_add = count_calls(add)
print(counted_add(1,2))
print(counted_add(3,4))