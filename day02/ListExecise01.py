list_person = []
while True:
    str_input = input("请输入人物名：")
    if str_input == "" :
        break
    list_person.append(str_input)
# for item in range(list_person):--报错
for item in list_person:
    print(item)
