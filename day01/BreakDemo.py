number = int(input("请输入整数："))
for item in range(2,number):
    if number % item == 0:
        #参数中加了end=""就可以不换行
        print("不",end="")
        break
print("是素数")