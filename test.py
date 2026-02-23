# 1
def calculator():
    while True:
        a = input("第一个数字：")
        if a.isdigit():
            a = float(a)
        else:
            print("请输入数字！")
            continue
        b = input("第二个数字：")
        if b.isdigit():
            b = float(b)
        else:
            print("请输入数字！")
            continue
        symbol = input("符号(+|-|*|/)：")
        if symbol == "+":
            print(a + b)
            break
        elif symbol == "-":
            print(a - b)
            break
        elif symbol == "*":
            print(a * b)
            break
        elif symbol == "/":
            if b == 0:
                print("除数不能为0")
                continue
            else:
                print(a / b)
                break
        else:
            print("请输入(+|-|*|/)中的一种！")
            continue




calculator()


# 2
def purity(a):
    for b in a:
        if b.isalpha():
            print(b)
        elif b.isdigit():
            c = b[0]
            for d in b:
                if d > c:
                    c = d
            print(c)
            for e in b:
                if e < c:
                    c = e
            print(c)

purity(["123213","e312","qsz"])