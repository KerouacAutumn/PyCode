import random
random_num = random.randint(1,100)
print(random_num)
count = 0
while count < 3:
    count += 1
    input_num = int(input("请输入数字："))
    if input_num < random_num:
        print("小了")
    elif input_num > random_num:
        print("大了")
    else:
        print("猜对了，总共猜了"+str(count)+"次")
        break
else:
    print("失败")
