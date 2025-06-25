str1 = input("")
arr1 = str1.split(" ")
arr2 = list(reversed(arr1))
str3 = ""
for i in arr2:
    if str3 == "":
        str3 += i
    else:
        str3 = str3 + " " + i
print(str3)
