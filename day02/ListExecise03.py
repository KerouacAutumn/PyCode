list_name = []
# while True:
#     name = input("请输入名字：")
#     if name == "":
#         break
#     if name in list_name:
#         print("姓名已经存在！！！")
#     else:
#         list_name.append(name)
# for item in list_name:
#     print(list_name)
# ['qwe', 'asd', 'zxc']
# ['qwe', 'asd', 'zxc']
# ['qwe', 'asd', 'zxc']
while True:
    name = input("请输入名字：")
    if name == "":
        break
    if name not in list_name:
        list_name.append(name)
    else:
        print("姓名已经存在！！！")
for item in range(-1, - len(list_name)-1, -1):
    print(list_name[item])
