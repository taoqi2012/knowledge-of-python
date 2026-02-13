# 预设起始单词（如 "apple"），提示用户输入下一个单词；
# 规则：新单词的首字母必须等于上一个单词的尾字母（如 apple 尾字母是 e，下一个可以是 egg）；
# 用 while 循环实现，直到用户输入错误为止，打印「接龙失败」。
def word_chain(first_word):
    repetitive_word = [first_word]
    while True:
        new_word = input(f"当前单词为{first_word},请输入接龙的单词:")
        if new_word in repetitive_word:
            print("接龙失败，游戏结束")
            break
        elif first_word[-1] == new_word[0]:
            print(f"接龙成功！当前单词更新为：{new_word}")
            first_word = new_word
            repetitive_word.append(new_word)
        else:
            print("接龙失败，游戏结束")
            break

word_chain("banana")



# 定义函数 sum_1_to_n(n)，接收正整数 n；
# 方法 1：用循环（for/while）累加 1+2+...+n；
# 方法 2：用数学公式 n*(n+1)/2 计算；
# 对比两种方法的结果，打印输出（如 n=100 → 结果 5050）。
def sum_1_to_n(n):
    a = n * (n + 1) / 2
    print(a)

sum_1_to_n(6794467946732)



# 定义函数 compound_interest(principal, rate, years, times)：
# principal：本金，rate：年利率（如 5% 传 0.05），years：年数，
#
#
# 公式：终值 = P×(1+r/n)n×t（P = 本金，r = 年利率，n = 每年复利次数，t = 年数）；
# 测试：本金 10000，年利率 5%，存 5 年，每年复利 12 次 → 终值≈12833.59。

def compound_interest(principal, rate, years):
    print(principal * (100 + rate) * years / 100)

compound_interest(100000000,2.33,10)



# 题目 2：计算 BMI 指数（身体质量指数）
# 要求
#
# 定义函数 calc_bmi(weight, height)：
# weight：体重（kg），height：身高（m）；
# 公式：体重身高²；
#
#
# 打印 BMI 值，并判断范围：
# <18.5：偏瘦；18.5-23.9：正常；24-27.9：超重；≥28：肥胖；
#
#
# 测试：体重 60kg，身高 1.7m → BMI≈20.76（正常）。
def calc_bmi(weight, height):
    print(weight / (height * height))

calc_bmi(50,1.55)