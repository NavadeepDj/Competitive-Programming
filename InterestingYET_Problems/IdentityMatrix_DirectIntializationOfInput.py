rows, cols = map(int, input().split())
# m = 
# arr = [[list(map(int, input().split())) for _ in range(cols)] for _ in range(rows)]
# print(arr)
am = False
arr =[]
while (am == False):
    for i in range(rows):
        while True:
            row = list(map(int, input().split()))
            if len(row) == cols:
                arr.append(row)
                break
            else:
                print(f"Please enter only {cols}")
    
            
    print("Array", arr)
    
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
