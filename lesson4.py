# 第四课：列表
fruits_list = ["苹果", "香蕉", "橘子", "葡萄"]
# 1 取元素
print("第一个水果是",fruits_list[0])
print("第三个水果是",fruits_list[2])
# 2 添加元素
fruits_list.append("西瓜")
print("现在有",len(fruits_list),"种水果","第三种水果是",fruits_list[2])
# 3 循环遍历
scores = [88,92,75,60,100]
total = 0
for i in scores:
    total += i
print("总分是",total)
# 4 算平均分
print("平均分是",total / len(scores))