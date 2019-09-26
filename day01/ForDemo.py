# str01 = "安河桥"
# for item in str01:
#     print(item)
# # range整数生成器  range(开始值，结束值，间隔）
# for item in range(1, 5, 2):
#     print(item)
#     # for + range执行预定次数
# thickness = 0.0001
# for item in range(30):
#     thickness *= 2
#     print(thickness)
# str = ","
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         if j != i:
#             print(j, "x", i, "=", "%d" % (i * j), str, end="\t")
#         elif j == i & i == 9:
#             print(j, "x", i, "=", "%d" % (i * j), "。", end="\t")
#     print()
for i in range(1, 10):
    for j in range(1, i + 1):
        if j == i & i == 9:
            print(j, "x", i, "=", "%d" % (i * j), "。", end="\t")
        else:
            print(j, "x", i, "=", "%d" % (i * j), ",", end="\t")
    print()
# for i in range(1,10):
#     for j in range(1,i+1):
#         if j!=i:
#             print(j,'*',i,'=','%d,'%(i*j),end='\t')
#         else:
#             print(j,'*',i,'=','%d'%(i*j),end='\t')
#     print()