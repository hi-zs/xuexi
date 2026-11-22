# 第三课：循环
for i in range(1, 11):
    print(i)
# 计算 1 加到 100 的和
total = 0
for i in range(1, 101):
    total = total + i
print("1 到 100 的和是", total)
for i in range(1, 4):      # 外层：1 到 3
    for j in range(1, 4):  # 内层：1 到 3
        print(i, "×", j, "=", i * j)
for i in range(1,101):
    if i%2==1:#奇数
        print(i)