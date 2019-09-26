day_of_month = (31,28,31,30,31,30,31,31,30,31,30,31)
month = int(input("请输入月："))
day = int(input("请输入日："))
result = day
for i in range(month-1):
    result += day_of_month[i]
print(result)