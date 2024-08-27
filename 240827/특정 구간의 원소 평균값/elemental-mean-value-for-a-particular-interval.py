n = int(input())

arr = list(map(int,input().split()))

result = 0
for i in range(n):
    for j in range(i,n):
        sum_val = 0
        avg_val = 0
        for k in range(i,j+1):
            sum_val += arr[k]
        avg_val = sum_val / j+1-i
        
        for l in range(i,j+1):
            if avg_val = arr[l]:
                result += 1
print(result)