import random

score = 0
for item in range(10):
    random_num01 = random.randint(1,100)
    random_num02 = random.randint(1,100)
    input_num = input("请输入"+str(random_num01)+"+"+str(random_num02)+"=?")
    if input_num == "":
        break

    if int(input_num) == random_num01 + random_num02:
        score += 10;

print("总分："+str(score))