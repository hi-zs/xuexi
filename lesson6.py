# 第六课：字典

# 1. 定义字典
student = {
    "name" : "小明",
    "age" : 18,
    "score" : 92,
    "city" : "重庆",
}

# 2. 按名字取值
print("姓名：",student["name"])
print("年龄:",student["age"])
print("成绩:",student["score"])

# 3. 新增和修改
student["hobby"] = "编程"
student["score"] = 95
print(student)

# 4. 遍历字典
for k,v in student.items():
    print(k,":",v)