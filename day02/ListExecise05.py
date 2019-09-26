list_input = []
for i in range(5):
    num_input = int(input("请输入第%d个数字"%(i+1)))
    list_input.append(num_input)
    list_input.sort(key=None,reverse=False)

print("输入数字中最大值为："+str(list_input[len(list_input)-1]))