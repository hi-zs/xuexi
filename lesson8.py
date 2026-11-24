# # while 循环：计数
# count = 0
# while count < 5:
#     print("第",count,"次")
#     count += 1

# 猜数字游戏
secret = 7
guess = 0
while guess != secret:
    guess = int(input("猜一个数字（1-10）："))
    if guess > secret:
        print("太大了")
    elif guess < secret:
        print("太小了")
print("猜对了！就是",secret)