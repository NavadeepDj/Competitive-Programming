rows, cols = map(int, input().split())

arr = [[0 for _ in range(cols)] for _ in range(rows)]
print(arr)
am = False
while (am == False):
    for i in range(rows):
        for j in range(cols):
            arr[i][j] = int(input())
    
            
    print("Atrr", arr)
    
    booli = True
    for i in range(rows):
        for j in range(cols):
            if i == j and arr[i][j] != 1:
                booli = False
            elif i != j and arr[i][j] != 0:
                booli = False
    if booli == True:
        print("Identity")
        am = True
    else:
        print("Not")


#3 3
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# 1
# 1
# 1
# 1
# 1
# 1
# 1
# 1
# 1
# Atrr [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
# Not
# 11
# 1
# 1
# 1
# 1
# 1
# 1
# 1
# 1
# Atrr [[11, 1, 1], [1, 1, 1], [1, 1, 1]]
# Not
# 1
# 1
# 1
# 1
# 1
# 1
# 1
# 1
# 1
# Atrr [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
# Not
# 1
# 1
# 1
# 1
# 1
# 1
# 1
# 1
# 1
# 1
# Atrr [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
# Not
# 1
# 1
# 1
# 1
# 1
# 1
# 11
# 1
# 1Atrr [[1, 1, 1], [1, 1, 1], [1, 11, 1]]
# Not



# Traceback (most recent call last):
#   File "/home/main.py", line 9, in <module>
#     arr[i][j] = int(input())
#                 ^^^^^^^^^^^^
# ValueError: invalid literal for int() with base 10: ''
# [?2004h
