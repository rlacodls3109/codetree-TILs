n, k = tuple(map(int,input().split()))

num = list(map(int,input().split()))

result = -1

# 
for i in range(n-k+1):
    sum_num = 0
    for j in range(i,i+k):
        sum_num += num[j]
    
    result = max(sum_num,result)

print(result)