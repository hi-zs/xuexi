# # 第一个小工具：记账小助手
# # 用一个列表存所有账目，每条是一个小列表【类型，金额，说明】
# records = []
# # 函数1： 记一笔账
# def add_record(kind,amount,note):
#     records.append([kind,amount,note])
# # 函数2： 查看所有明细
# def show_records():
#     for r in records:
#         print(r)
# # 函数3： 算总余额
# def show_balance():
#     total = 0
#     for r in records:
#         kind = r[0]
#         amount = r[1]
#         if kind == "收入":
#             total = total + amount
#         else:
#             total = total - amount
#     return total
# # 测试
# # add_record("支出",30,"晚饭")
# # show_records()
# # print("当前余额是",show_balance())
#
# # 让程序能交互：循环输入记账
# while True:
#     print("\n===  记账小助手  ===")
#     print("1. 记一笔账")
#     print("2. 查看明细")
#     print("3. 查看余额")
#     print("4. 退出")
#     choice = input("请选择（1-4）：")
#     if choice == "1":
#         kind = input("类型（收入/支出）")
#         amount = float(input("金额："))
#         note = input("说明：")
#         add_record(kind,amount,note)
#         print("已记账！")
#     elif choice == "2":
#         show_records()
#     elif choice == "3":
#         print("当前余额是",show_balance())
#     elif choice == "4":
#         print("再见！")
#         break
# from ctypes import kind


# 记账小助手（带文件存储版）

# 1. 从文件加载之前的账（如果文件不存在，就用空列表）
def load_records():
    records = []
    try:
        with open("records.txt","r") as f:
            for line in f:
                line = line.strip()         # 去掉末尾换行符
                if line == "":
                    continue                # 跳过空行
                parts = line.split(",")
                parts[1] = float(parts[1])  # 金额转回数字
                records.append(parts)
    except FileNotFoundError:
        pass    # 文件还不存在，说明是第一次用，直接用空列表
    return records

# 2.把账保存到文件
def save_records(records):
    with open("records.txt","w") as f:
        for r in records:
            f.write(str(r[0]) + "," + str(r[1]) +","+ str(r[2]) + "\n")

# 3.记一笔账
def add_record(records,kind,amount,note):
    records.append([kind,amount,note])

# 4. 查看明细
def show_records(records):
    for r in records:
        print(r)

# 5. 算余额
def show_balance(records):
    total = 0
    for r in records:
        if r[0] == "收入":
            total += r[1]
        else:
            total -= r[1]
    return total
# 6 暂停：等用户回车再继续
def pause():
    choice = input("\n按回车键继续，或按4退出：")
    if choice == "4":
        exit()   #直接结束程序

# =====  主程序  =====
records = load_records()
while True:
    print("\n=== 记账小助手 ===")
    print("1. 记一笔账")
    print("2. 查看明细")
    print("3. 查看余额")
    print("4. 退出")
    choice = input("请选择（1-4）：")

    if choice == "1":
        kind = input("类型（收入/支出）：")
        amount = float(input("金额："))
        note = input("说明：")
        add_record(records,kind,amount,note)
        save_records(records)       # 记账后立刻保存
        print("已记账并保存！")
        pause()
    elif choice == "2":
        show_records(records)
        pause()
    elif choice == "3":
        print("当前余额是",show_balance(records))
        pause()
    elif choice == "4":
        print("再见！")
        break