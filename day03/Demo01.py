"""
在控制台中录入多个学生姓名，如果有重复的姓名，不存入列表，
如果输入esc，则停止录入，在每行打印学生姓名

"""
list_stu_name = []
while True:
    name = input("请输入姓名：")
    if name == "esc":
        break
    if name in list_stu_name:
        print("已存在，请重新输入：")
        continue
    list_stu_name.append(name)
# 倒叙获取列表中的元素
for item in range(len(list_stu_name) - 1, - 1, -1):
    print(list_stu_name[item])
