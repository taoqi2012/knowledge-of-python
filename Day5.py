# 1. 什么是 range？
# range是 Python 内置函数，核心作用是：生成一个不可变的整数序列（不是列表，是 “可迭代对象”），
# 通常用于for循环中控制循环次数、生成连续 / 间隔的整数。
# 通俗理解：range就像一个 “整数生成器”，你告诉它 “起始数、结束数、步长”，它就能按规则生成一串整数；
# 关键特点：range生成的序列不占内存（按需生成），比直接写列表[1,2,3]更高效，尤其生成大数序列时。

# 2. 基础语法（三种形式）
# a.range(stop)	stop：结束数（必传）
# 生成0-4的整数序列（不包含5）
nums = range(5)
# 打印range对象（不是列表，需转列表查看）
print(nums)          # 输出：range(0, 5)
print(list(nums))    # 输出：[0, 1, 2, 3, 4]

# 配合for循环：循环5次（计数从0到4）
for i in range(5):
    print(f"循环次数：{i+1}")  # i+1把0-4转成1-5，更符合日常计数习惯

# b.range(start, stop)	start：起始数，stop：结束数
# 生成2-5的整数序列（包含2，不包含6）
nums = range(2, 6)
print(list(nums))  # 输出：[2, 3, 4, 5]

# 配合for循环：遍历1-10的整数
for num in range(1, 11):
    print(num, end=" ")  # 输出：1 2 3 4 5 6 7 8 9 10

# c.range(start, stop, step)	start：起始数，stop：结束数，step：步长
# 场景 1：生成奇数（步长 2，起始 1）
# 1-10的奇数（1,3,5,7,9）
nums = range(1, 10, 2)
print(list(nums))  # 输出：[1, 3, 5, 7, 9]
# # 0-10的偶数（0,2,4,6,8,10）
# nums = range(0, 11, 2)
# print(list(nums))  # 输出：[0, 2, 4, 6, 8, 10]
# 场景 2：生成偶数（步长 2，起始 0）
# 10-1的递减序列（步长-1）
nums = range(10, 0, -1)
print(list(nums))  # 输出：[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# 10-2的递减偶数（步长-2）
nums = range(10, 1, -2)
print(list(nums))  # 输出：[10, 8, 6, 4, 2]

# 场景 3：生成递减序列（步长为负）
# 10-1的递减序列（步长-1）
nums = range(10, 0, -1)
print(list(nums))  # 输出：[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# 10-2的递减偶数（步长-2）
nums = range(10, 1, -2)
print(list(nums))  # 输出：[10, 8, 6, 4, 2]

# 案例 1：用 range 生成 1-100 的累加和
a = 0
for number in range(1,101):
    a += number
print(a)

# 案例 2：用 range 生成指定长度的随机验证码（结合 random）
import random
def ran_num(length):
    password = ""
    for _ in range(length):
        password += str(random.randint(0, 9))
    print(password)
ran_num(8)

# 案例 3：用 range 遍历列表（按索引访问）
fruits = ["苹果", "香蕉", "橙子", "葡萄"]
# 用range生成列表索引（0-3）
for i in range(len(fruits)):
    print(f"索引{i}：{fruits[i]}")

# 案例 4：用 range 实现乘法口诀表
# 九九乘法表（用双层range循环）
for i in range(1, 10):  # 行：1-9
    for j in range(1, i+1):  # 列：1到当前行号
        print(f"{j}×{i}={i*j}", end="\t")
    print()  # 换行