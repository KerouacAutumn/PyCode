# str_result = ""
list_result = []
for item in range (10):
    list_result.append(str(item))
str_result = "".join(list_result)
print(str_result)
str = "how are you"
list_result = str.split(" ")
str_result = " ".join(list_result[::-1])
print(str_result)