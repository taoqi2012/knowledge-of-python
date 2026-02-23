# 题目 1：基础继承（单继承 + 方法重写）
# 需求：
# 定义一个基类 Animal，包含：
# 初始化方法 __init__，接收 name（名字）和 age（年龄）两个属性
# 一个方法 make_sound()，默认返回字符串 "未知叫声"
# 一个方法 show_info()，返回格式为 "名字：xxx，年龄：x岁" 的字符串
# 定义子类 Dog 继承自 Animal，并重写：
# make_sound() 方法，返回 "汪汪汪"
# 新增一个方法 fetch()，返回 "[名字] 叼来了球"（使用自身的 name 属性）
# 定义子类 Cat 继承自 Animal，并重写：
# make_sound() 方法，返回 "喵喵喵"
# 编写测试代码：
# 创建一个 Dog 实例（名字：旺财，年龄：3），调用 make_sound()、show_info()、fetch() 并打印结果
# 创建一个 Cat 实例（名字：咪咪，年龄：2），调用 make_sound()、show_info() 并打印结果
from turtledemo.penrose import start


class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def make_sound(self):
        print("未知叫声")
    def show_info(self):
        return f"名字：{self.name}，年龄：{self.age}岁"

class Dog(Animal):
    def make_sound(self):
        print("汪汪汪")
    def fetch(self):
        print(f"{self.name}叼来了球")

class Cat(Animal):
    def make_sound(self):
        print("喵喵喵")

dog1 = Dog("旺财","3岁")
dog1.make_sound()
dog1.show_info()
dog1.fetch()

cat1 = Cat("咪咪","4岁")
cat1.make_sound()
cat1.show_info()

# 题目 2：组合的应用（“有一个” 关系）
# 需求：
# 定义一个类 Engine（发动机），包含：
# 初始化方法 __init__，接收 power（功率，单位：马力）
# 方法 start()，返回 "发动机启动，功率：x马力"
# 方法 stop()，返回 "发动机关闭"
# 定义一个类 Car（汽车），通过组合的方式 使用 Engine：
# 初始化方法 __init__，接收 brand（品牌）、color（颜色）、engine_power（发动机功率）
# 在 Car 的初始化方法中，创建一个 Engine 实例作为 Car 的属性
# 方法 start_car()，返回 "[品牌] [颜色] 汽车启动：[发动机启动的返回值]"
# 方法 stop_car()，返回 "[品牌] [颜色] 汽车熄火：[发动机关闭的返回值]"
# 编写测试代码：
# 创建一个 Car 实例（品牌：特斯拉，颜色：白色，发动机功率：200）
# 调用 start_car() 和 stop_car() 并打印结果
class Engine:
    def __init__(self,power):
        self.power = power
    def start(self):
        return f"发动机启动，功率：{self.power}马力"
    def stop(self):
        return "发动机关闭"

class Car(Engine):
    def __init__(self,brand,color,power):
        self.brand = brand
        self.color = color
        super().__init__(power)
    def start_car(self):
        print(f"{self.brand} {self.color} 汽车启动：{self.start()}")
    def stop_car(self):
        print(f"{self.brand} {self.color} 汽车熄火：{self.stop()}")

car1 = Car("特斯拉","红色",200)
car1.start_car()
car1.stop_car()

# 题目 3：继承 + 组合综合应用（进阶）
# 需求：
# 基于题目 1 的 Animal 基类，定义一个新的子类 Pet（宠物），包含：
# 初始化方法 __init__，接收 name、age、owner（主人，字符串类型）
# 方法 show_owner()，返回 "[名字] 的主人是：[owner]"
# 定义一个类 Home（家庭），组合 多个 Pet 实例：
# 初始化方法 __init__，接收 family_name（家庭名称）
# 一个属性 pets，初始化为空列表，用于存储宠物实例
# 方法 add_pet(pet)，将 Pet 实例添加到 pets 列表中
# 方法 show_all_pets()，遍历 pets 列表，打印每个宠物的 show_info() 和 show_owner() 结果，格式为：
# plaintext
# 【xx家庭的宠物列表】
# 1. 名字：xxx，年龄：x岁 | 主人：xxx
# 2. 名字：xxx，年龄：x岁 | 主人：xxx
# 编写测试代码：
# 创建两个 Pet 实例（比如：宠物 1：名字 “旺财”，年龄 3，主人 “张三”；宠物 2：名字 “咪咪”，年龄 2，主人 “张三”）
# 创建一个 Home 实例（家庭名称：张三家庭）
# 将两个宠物添加到家庭中，调用 show_all_pets() 打印结果
class Pet(Animal):
    def __init__(self,name,age,owner):
        super().__init__(name,age)
        self.owner = owner
    def show_owner(self):
        return f"{self.name}的主人是:{self.owner}"

class Home:
    def __init__(self,family_name):
        self.family_name = family_name
        self.pets = []
    def add_pet(self,pet):
        self.pets.append(pet)
    def show_all_pets(self):
        for pet in self.pets:
            print(f" {pet.show_info()},{pet.show_owner()}")

pet1 = Pet("旺财", 3, "张三")
pet2 = Pet("咪咪", 2, "张三")
home = Home("张三家庭")
home.add_pet(pet1)
home.add_pet(pet2)
home.show_all_pets()