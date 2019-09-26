number = int(input("请输入星星数量："))
print("*" * number)
for item in range(number - 2):
    print("*" + " " * (number - 2) + "*")
print("*" * number)
