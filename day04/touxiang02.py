from PIL import Image

# 创建图片对象
headImage = Image.open('E:\PythonProject\PyCode\static\idea.png')
markImage = Image.open('E:\PythonProject\PyCode\static\guoqi.png')
# 获取图片对象的宽高
w1, h1 = headImage.size
w2, h2 = markImage.size
print("头像的宽%d高%d" % (w1, h1))
print("国旗的宽%d高%d" % (w2, h2))

print(headImage)
print(markImage)

box = (w1-w2, h1-h2)
print(box)

region = markImage
region = region.resize((w2, h2))
headImage.paste(region, box)
headImage.save('E:\PythonProject\PyCode\static\myidea.png')

# def addImg(img):
#     img.paste(markImage, (0, 0))
# addImg(headImage)
# headImage.save('E:\PythonProject\PyCode\static\myidea02.png')
# final2 = Image.new("RGBA", headImage.size)
#
# final2 = Image.alpha_composite(final2, headImage)
#
# final2 = Image.alpha_composite(final2, markImage)
#
# final2.show()
#
# final2.save("E:\PythonProject\PyCode\static\myidea02.png")
