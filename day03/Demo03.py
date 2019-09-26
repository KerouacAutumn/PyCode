"""
列表推导式
"""
list01 = [4, 123, 12, 35, 68, 45, 9, 8]
list02 = [item ** 2 for item in list01]
print(list02)
list03 = [item ** 2 for item in list01 if item > 10]
print(list03)
list04 = []
for item in list01:
    list04.append(item % 10)
print(list04)
list05 = [item % 10 for item in list01]
print(list05)
