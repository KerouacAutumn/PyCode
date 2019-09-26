list_score = []
while True:
    score_input = input("请输入成绩")
    # score = int(score_input)
    if score_input == "":
        break
    if int(score_input) < 0 or int(score_input) > 100:
        print("输入错误，请重新输入")
    else:
        list_score.append(int(score_input))
    # if score_input == "":
    #     break
    # list_score.append(int(score_input))
for item in list_score:
    print(item)
print("最高分" + str(max(list_score)))
print("最低分" + str(min(list_score)))
print("平均分" + str(sum(list_score) / len(list_score)))
