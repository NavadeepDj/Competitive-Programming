# Moving zeroes towards end without changing the rder
#Time complexity is n^2
list1 = [0,0,5,1,0,2,0,1]

for i in range(len(list1)):
    if list1[i] == 0:
        for j in range(i+1, len(list1)):
            if list1[j] != 0:
                temp = list1[i]
                list1[i] = list1[j]
                list1[j] = temp
                break
            print("First", list1)

print(list1)
