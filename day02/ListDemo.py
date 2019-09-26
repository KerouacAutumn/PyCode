"""
    列表
"""
# 空
list01 = []
list01 = list()

list02 = ["悟空", 100, True]
# list02 = list("悟空",100,True)
list02 = list("我是齐天大圣")
# 获取元素 索引/切片
print(list02[2])  # 齐
print(list02[-4:])  # ['齐', '天', '大', '圣']
list02.append("孙悟空")
print(list02)
list02.insert(-2, "花果山美猴王")
print(list02)
# list02.remove("孙悟空")
# del list02[-3]
del list02[0:-3]
print(list02)
list02[1:3] = []
print(list02)

list03 = list("我是齐天大圣")
for item in list03:
    print(item)
for item in list03[::-1]:  # list03[::-1]重新创建了新列表
    print(item)
