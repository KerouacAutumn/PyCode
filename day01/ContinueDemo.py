sum_value = 0
# for item in range(1,101):
#     if item % 5 != 0:
#         continue
#     sum_value += item
#
# print(sum_value)
for item in range(10, 51):
    unit = item % 10
    if unit == 2 or unit == 5 or unit == 9:
        continue
    # elif item % 10 == 5:
    #     continue
    # elif item % 10 == 9:
    #     continue
    sum_value += item;
print(sum_value)
