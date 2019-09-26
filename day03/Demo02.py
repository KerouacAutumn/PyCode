"""
将list_sc中大于60的元素存入list01中
获取list_sc中的最大值（不适用max）
"""
list_sc = [60, 58, 85, 35, 26, 20, 90]
list01 = []
# for item in list_sc:
#     # print(item)
#     if item > 60:
#         # print(item)
#         list01.append(item)
# for i in list01:
#     print(i)
max_val = list_sc[0]
for i in range(1, len(list_sc)):
    if max_val < list_sc[i]:
        max_val = list_sc[i]
print(max_val)
