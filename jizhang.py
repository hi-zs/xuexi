# 第一个小工具：记账小助手
# 用一个列表存所有账目，每条是一个小列表【类型，金额，说明】
records = [
    ["收入", 8000, "工资"],
    ["支出", 25.5, "午饭"],
    ["支出", 120, "地铁卡"],
]
# 函数1： 记一笔账
def add_record(kind,amount,note):
    records.append([kind,amount,note])
# 函数2： 查看所有明细
def show_records():
    for r in records:
        print(r)
# 函数3： 算总余额
def show_balance():
    total = 0
    for r in records:
        kind = r[0]
        amount = r[1]
        if kind == "收入":
            total = total + amount
        else:
            total = total - amount
    return total
# 测试
# add_record("支出",30,"晚饭")
# show_records()
# print("当前余额是",show_balance())

# 让程序能交互：循环输入记账
while True:
    print("\n===  记账小助手  ===")
    print("1. 记一笔账")
    print("2. 查看明细")
    print("3. 查看余额")
    print("4. 退出")
    choice = input("请选择（1-4）：")
    if choice == "1":
        kind = input("类型（收入/支出）")
        amount = float(input("金额："))
        note = input("说明：")
        add_record(kind,amount,note)
        print("已记账！")
    elif choice == "2":
        show_records()
    elif choice == "3":
        print("当前余额是",show_balance())
    elif choice == "4":
        print("再见！")
        break
