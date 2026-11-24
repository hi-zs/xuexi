# 第七课：字符串操作

# 1. f-string 拼接
name = "山寻"
age = 33
city = "重庆"
print(f"我的名字叫{name},我今年{age}岁,我来自{city}")

# 2. 判断包含
s = "我正在学习Python编程"
print("Python" in s)
print("Java" in s)

# 3. 替换
s2 = s.replace("Python","AI")
print(s2)

# 4. 切片
print(s[0:4])
print(s[4:])