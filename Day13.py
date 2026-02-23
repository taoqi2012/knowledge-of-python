# 1. 函数可以做为参数进行传递
# 2. 函数可以作为返回值进行返回
# 3. 函数名称可以当成变量一样进行赋值操作
def guanjia(game):
    # inner函数必须缩进（属于guanjia的内部函数）
    def inner():
        print("打开外挂")  # 修正：中文引号→英文双引号，补充缺失的引号
        game()  # 执行被装饰的函数
        print("关闭外挂")  # 修正：中文引号→英文双引号，补充缺失的引号
    # 返回inner函数（注意缩进，属于guanjia函数的返回）
    return inner

# 修正：play_dnf后去掉多余空格，字符串单引号统一为英文单引号
@guanjia  # 相当于 play_dnf = guanjia(play_dnf)
def play_dnf():
    print('你好啊,我叫赛利亚,今天又是美好的一天!')

@guanjia
def play_lol():
    print("德玛西亚 !!!!!! ")  # 双引号也可以，Python中单/双引号通用

play_dnf()
play_lol()



# 编程练习题：日志装饰器
# 题目要求
# 定义一个装饰器 add_log，作用是为函数添加 “运行日志” 功能：
# 调用被装饰的函数前，打印：[开始执行] 函数名：xxx
# 调用被装饰的函数后，打印：[执行结束] 函数名：xxx
# 定义两个普通函数，并用 add_log 装饰：
# cook_food()：打印 “正在做番茄炒蛋...”
# clean_room()：打印 “正在打扫客厅...”
# 调用这两个函数，验证装饰器效果，最终输出需符合以下格式：
# [开始执行] 函数名：cook_food
# 正在做番茄炒蛋...
# [执行结束] 函数名：cook_food
# ---
# [开始执行] 函数名：clean_room
# 正在打扫客厅...
# [执行结束] 函数名：clean_room
def add_log(thing):
     def inner():
        print("开始执行 ")
        thing()
        print("执行结束")
     return inner()

@add_log
def cook_food():
    print("正在做番茄炒蛋...")

@add_log
def clean_room():
    print("正在打扫客厅...")

cook_food()