# 通讯录管理器（完整版）

# ============ 一、数据读写 ============
def load_contacts():
    result = []
    try:
        with open("contacts.txt", "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line == "":
                    continue
                parts = line.split(",")
                result.append({"name": parts[0], "phone": parts[1]})
    except FileNotFoundError:
        pass
    return result

def save_contact():
    with open("contacts.txt", "w", encoding="utf-8") as f:
        for c in contacts:
            f.write(c["name"] + "," + c["phone"] + "\n")

# ============ 二、功能函数 ============
def add_contact(name, phone):
    contacts.append({"name": name, "phone": phone})
    save_contact()
    print("已添加", name)

def show_contacts():
    if len(contacts) == 0:
        print("通讯录是空的")
        return
    for c in contacts:
        print(c["name"], "的电话是", c["phone"])

def find_contact(name):
    found = False
    for c in contacts:
        if c["name"] == name:
            print(c["name"], "的电话是", c["phone"])
            found = True
    if not found:
        print("没找到这个人")

def delete_contact(name):
    for c in contacts:
        if c["name"] == name:
            contacts.remove(c)
            save_contact()
            print("已删除", name)
            return
    print("没找到这个人")

# ============ 三、主程序 ============
contacts = load_contacts()

while True:
    print("\n=== 通讯录管理器 ===")
    print("1. 添加联系人")
    print("2. 查看所有联系人")
    print("3. 查找联系人")
    print("4. 删除联系人")
    print("5. 退出")
    choice = input("请选择(1-5)：")

    if choice == "1":
        name = input("姓名：")
        phone = input("电话：")
        add_contact(name, phone)
    elif choice == "2":
        show_contacts()
    elif choice == "3":
        find_contact(input("输入要查找的姓名："))
    elif choice == "4":
        delete_contact(input("输入要删除的姓名："))
    elif choice == "5":
        print("再见！")
        break
