# if嵌套
# 基本结构
'''
# 外层条件
if 条件1:
    # 条件1满足时执行
    代码块1

    # 内层嵌套条件（只有条件1满足，才会执行这里）
    if 条件2:
        代码块2  # 条件1+条件2都满足
    else:
        代码块3  # 条件1满足，但条件2不满足

else:
    # 条件1不满足时执行
    代码块4  # 内层代码完全不执行
'''

# 练习1：
# 外层：判断是否及格（分数≥60）；
# 内层：及格的前提下，判断是否优秀（分数≥90）；不及格则直接提示。
score = int(input("请输入分数"))
if score >= 60:
    if score >= 90:
        print("优秀")
    else:
        print("及格")
else:
    print("不及格")
# 练习2：
# 外层：先判断密码长度是否在 8-20 位（基础条件）；
# 内层 1：长度合格的前提下，判断是否包含数字；
# 内层 2：包含数字的前提下，再判断是否包含大写字母；
# 任何一层条件不满足，直接提示具体问题。
def check_password_strength():
    password = input("请输入密码：")

    # 外层条件1：判断长度是否合规（基础条件）
    if 8 <= len(password) <= 20:
        print("✅ 密码长度合规")

        # 内层嵌套1：判断是否包含数字
        has_number = any(char.isdigit() for char in password)#isdigit： 判断一个字符串 / 单个字符是否只包含数字字符（0-9）
        if has_number:
            print("✅ 密码包含数字")

            # 内层嵌套2：判断是否包含大写字母
            has_upper = any(char.isupper() for char in password)#isupper“检查字符是不是大写英文字母
            if has_upper:
                print("🎉 密码强度：强（长度+数字+大写字母）")
            else:
                print("⚠️ 密码强度：中（长度+数字，建议加大写字母）")

        # 内层else1：长度合规但无数字
        else:
            print("❌ 密码无数字，强度不足！")

    # 外层else1：长度不合规
    else:
        print("❌ 密码长度必须在8-20位之间！")

check_password_strength()

# 练习三
# 外层：判断年龄；
# 内层：不同年龄区间内，再判断是否有学生证 / 老年证。
age = int(input("请输入年龄："))
has_card = input("是否有学生证/老年证（是/否）：").strip() == "是"

# 外层：年龄分区间
if age < 18:
    print("未成年人")
    # 内层：未成年人是否有学生证
    if has_card:
        print("票价：免费")
    else:
        print("票价：半价")

elif 18 <= age <= 60:
    print("成年人")
    # 内层：成年人是否有优惠证（这里假设无）
    print("票价：全价")

else:
    print("老年人")
    # 内层：老年人是否有老年证
    if has_card:
        print("票价：免费")
    else:
        print("票价：半价")

# random
import random # 导入整个random模块
# 1. 生成随机浮点数：random.random()
# 作用：生成 0 ≤ x < 1 之间的随机浮点数（小数）
import random
num = random.random()
for num in range(5):
    print(random.random())

# 生成指定范围的浮点数
# 公式：最小值 + random.random() * (最大值 - 最小值)
num = 10 + random.random() * 10
print(num)  # 示例输出：15.6789（10≤x<20）

# 生成指定范围的随机整数
import random
# 生成1-100之间的随机整数（包含1和100）
num = random.randint(1, 100)
print(num)  # 示例输出：45

# 生成5个10-20之间的随机整数
for _ in range(5):
    print(random.randint(10, 20))

# 3. 随机选择元素：random.choice(序列)
# 作用：从列表、字符串、元组等序列中随机选 1 个元素
import random

# 从列表中随机选1个
fruits = ["苹果", "香蕉", "橙子", "葡萄"]
fruit = random.choice(fruits)
print(f"随机选的水果：{fruit}")  # 示例输出：随机选的水果：香蕉

# 从字符串中随机选1个字符（生成随机字母）
letter = random.choice("abcdefghijklmnopqrstuvwxyz")
print(f"随机小写字母：{letter}")  # 示例输出：随机小写字母：k

# 从元组中随机选1个
nums = (10, 20, 30, 40)
print(random.choice(nums))  # 示例输出：30

# 4. 随机选择多个不重复元素：random.sample(序列, k)
# 作用：从序列中随机选k个不重复的元素，返回列表
import random

# 从列表中随机选2个不重复的水果
fruits = ["苹果", "香蕉", "橙子", "葡萄"]
selected = random.sample(fruits, 2)
print(f"随机选2个水果：{selected}")  # 示例输出：随机选2个水果：['橙子', '苹果']

# 从1-10中随机选3个不重复的数
nums = random.sample(range(1, 11), 3)
print(nums)  # 示例输出：[5, 8, 2]

# 5. 打乱序列：random.shuffle(列表)
import random

# 打乱列表
nums = [1, 2, 3, 4, 5]
random.shuffle(nums)
print(f"打乱后的列表：{nums}")  # 示例输出：打乱后的列表：[3, 1, 5, 2, 4]

# 打乱字符串（需先转列表，再转回字符串）
s = "abcde"
s_list = list(s)
random.shuffle(s_list)
new_s = "".join(s_list)
print(f"打乱后的字符串：{new_s}")  # 示例输出：打乱后的字符串：dceab

# 6. 生成指定步长的随机整数：random.randrange(start, stop, step)
# 作用：从start开始，以step为步长，到stop结束（不包含 stop），随机选 1 个整数
num = random.randrange(1, 11, 2)
print(num)  # 示例输出：7（只能是1/3/5/7/9）