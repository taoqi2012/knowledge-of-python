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

# 1. 类
class User:
    """这是一个用户类，封装了用户的属性和行为（文档字符串，可选）"""

    # 类属性：所有实例共享的属性（比如默认角色）
    default_role = "普通用户"

    # 构造方法：创建实例时自动调用，初始化实例属性
    def __init__(self, username, password):
        # 实例属性：每个用户独有的属性（用户名、密码），用self.绑定
        self.username = username
        self.password = password

    # 方法1：打印用户信息（无返回值）
    def print_info(self):
        # 通过self访问实例属性和类属性
        print(f"用户名：{self.username}")
        print(f"密码：{self.password}（已隐藏部分字符）")
        print(f"用户角色：{self.default_role}")


    # 方法2：检查密码长度是否合规（有返回值）
    def check_password_length(self):
        password_length = len(self.password)
        if 8 <= password_length <= 20:
            return True, "密码长度合规"
        else:
            return False, f"密码长度不合规（当前{password_length}位，要求8-20位）"
user1 = User("taoqi","20125017")
print(user1.print_info())
print(user1.check_password_length())

#实现用户类的继承
class Adminuser(User):
    default_role = "管理员"
    def __init__(self,username,password,admin_level):
        super().__init__(username,password)
        self.admin_level = admin_level
    def delete_user(self,target_username):
        print(f"✅ 管理员{self.username}（{self.admin_level}级）已删除用户：{target_username}")
admin1 = Adminuser("Peter","12345678","最高")
print(admin1.print_info())
print(admin1.delete_user("taoqi"))

# 定义一个Book类，封装图书的核心属性（书名、作者、页数、是否借出）。
# 定义类的方法，实现核心功能（打印图书信息、标记借出、标记归还、检查是否可借出）。
# 实例化多个图书对象，测试类的所有功能，体现类的封装性和复用性。
class Book:
    def __init__(self,name,author,pages,):
        self.name = name
        self.author = author
        self.pages = pages
        self.is_borrowed = False
    def print_info(self):
        borrow_status = "已借出" if self.is_borrowed else "未借出"
        print(f"书名:{self.name}")
        print(f"作者：{self.author}")
        print(f"页数：{self.pages}页")
        print(f"状态：{borrow_status}")
    def borrow_book(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"✅ 《{self.name}》借出成功！")
            return True
        else:
            print(f"❌ 《{self.name}》已被借出，无法重复借出！")
            return False
    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"✅ 《{self.name}》归还成功！")
            return True
        else:
            print(f"❌ 《{self.name}》未被借出，无需归还！")
            return False
book1 = Book("动物庄园","Lisa","400")
print(book1.print_info())
print(book1.borrow_book())
print(book1.borrow_book())
print(book1.return_book())