list1 = list(map(int, input().split()))
n = len(list1)
list1 = sorted(list1)
print(list1)
# if n % 2 == 0:
list1 = list1[n-1:(n//2)-1:-1]  + list1[:(n//2):1]
print(list1)

# 1 2 3 4 5 6 7
# [1, 2, 3, 4, 5, 6, 7]
# [7, 6, 5, 4, 1, 2, 3]  
