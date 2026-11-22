# def calculate_BMI():
#     height = float(input("请输入您的身高（m）：") )
#     weight = float(input("请输入您的体重（kg）：") )
#     BMI = float(weight/(height**2))
#     print("您的BMI值为：", BMI)
#     return BMI
# BMI = calculate_BMI()
# if BMI <= 18.5:
#     print("您的身体偏瘦")
# elif 18.5 < BMI <= 25:
#     print("您的身体正常")
# elif 25 < BMI <= 30:
#     print("您的身体偏胖")
# else:
#     print("您的身体肥胖")
def calculate_BMI(height,weight):
    BMI = (weight / height ** 2)
    if BMI <= 18.5:
        category = "偏瘦"
    elif BMI <= 25:
        category = "正常"
    elif BMI <= 30:
        category = "偏胖"
    else:
        category = "偏胖"
    print(f"您的BMI分类为：{category}")
    return BMI
pp = calculate_BMI(1.68,75)
print(pp)
