#  第五课：函数
# 1 无参数，无返回值的函数
def say_hello():
    print("你好，山寻！")

say_hello()

# 2 带参数的函数
def greet(name):
    print("你好，",name)
greet("小明")
greet("小红")

# 3 带返回值的参数，计算平均分
def calc_avg(scores):
    total = 0
    for s in scores:
        total += s
    return total/len(scores)
a = calc_avg([88,92,75,60,100])
print("第一组平均分是",a)
b = calc_avg([80,85,97,93,100])
print("第二组平均分是",b)
