height = 100
count = 0
sum = height
# while height > 0.01:
while height / 2 > 0.01:
    count += 1
    height /= 2
    sum += height*2#累加起落高度
    print("第%d次弹起的高度是%f,最终走了%f米" % (count, height,sum))
print("总共弹起来了%d次" % count)
