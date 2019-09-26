season = input("请输入季节：")
dict_seasons = {
    "春": (1, 2, 3),
    "夏": (4, 5, 6),
    "秋": (7, 8, 9),
    "冬": (10, 11, 12)
}
if season in dict_seasons:
    months = dict_seasons[season]
    for item in months:
        print(str(item) + "月份")
else:
    print("输入错误")
