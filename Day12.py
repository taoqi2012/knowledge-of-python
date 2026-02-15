# 一、先理解闭包（Closure）
# 闭包是实现装饰器的基础，我们先搞懂它。
# 1. 闭包的定义
# 简单来说，闭包就是一个嵌套函数，内部函数引用了外部函数的变量，并且外部函数返回了这个内部函数。
# 可以把闭包想象成：外部函数是一个 “工厂”，内部函数是 “产品”，工厂生产产品时，还把自己的 “原材料”（变量）打包给了产品。
# 2. 闭包的简单示例
def outer_func(msg):
    # 外部函数的变量
    message = msg

    # 内部函数，引用了外部函数的message变量
    def inner_func():
        print(f"收到的消息：{message}")

    # 外部函数返回内部函数（注意：不加括号，返回的是函数对象，不是执行结果）
    return inner_func


# 调用外部函数，得到内部函数对象，赋值给hello_func
hello_func = outer_func("你好！")
# 执行内部函数
hello_func()  # 输出：收到的消息：你好！

# 再创建一个新的闭包
hi_func = outer_func("嗨！")
hi_func()  # 输出：收到的消息：嗨！

# 3. 闭包的关键解释
# outer_func 是外部函数，接收参数msg并赋值给message；
# inner_func 是内部函数，没有自己的参数，但引用了外部函数的message变量；
# outer_func 返回的是inner_func函数对象（不是执行inner_func()），所以hello_func本质上就是inner_func；
# 即使outer_func执行完了，inner_func依然能访问到message变量，这就是闭包的核心特性 ——保留外部函数的变量环境。

# 3. 带参数的装饰器
# 如果想让装饰器更灵活（比如自定义日志前缀），需要再套一层函数：

# 带参数的装饰器（三层嵌套）
def log_decorator_with_prefix(prefix):
    # 接收装饰器的参数
    def decorator(func):
        def wrapper(*args, **kwargs):
            # 使用装饰器的参数
            print(f"【{prefix}】函数 {func.__name__} 即将执行")
            result = func(*args, **kwargs)
            print(f"【{prefix}】函数 {func.__name__} 执行完成")
            return result
        return wrapper
    return decorator

# 使用带参数的装饰器
@log_decorator_with_prefix("自定义日志")
def multiply(a, b):
    """计算两个数的积"""
    return a * b

result = multiply(4, 6)
print(f"计算结果：{result}")

# 输出：
# 【自定义日志】函数 multiply 即将执行
# 【自定义日志】函数 multiply 执行完成
# 计算结果：24

# 4. 保留原函数的元信息
# 装饰器会覆盖原函数的__name__、__doc__等元信息，解决方法是用functools.wraps：
import functools

def log_decorator(func):
    # 保留原函数的元信息
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"【日志】函数 {func.__name__} 即将执行")
        result = func(*args, **kwargs)
        print(f"【日志】函数 {func.__name__} 执行完成")
        return result
    return wrapper

@log_decorator
def add(a, b):
    """计算两个数的和"""
    return a + b

# 查看原函数的元信息
print(add.__name__)  # 输出：add（如果不用wraps，会输出wrapper）
print(add.__doc__)   # 输出：计算两个数的和