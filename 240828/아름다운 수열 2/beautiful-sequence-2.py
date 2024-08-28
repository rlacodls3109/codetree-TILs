n, m = tuple(map(int,input().split()))
A = list(map(int,input().split()))
B = list(map(int,input().split()))

result = 0

for i in range(n-m+1):
    check_in_B = True
    for j in range(i,i+m):
        if A[j] not in B:
            check_in_B = False
            break
    
    if check_in_B :
        result += 1

print(result)