n, k = tuple(map(int,input().split()))

num = list(map(int,input().split()))

result = -1

# 구간의 시작점 잡기
for i in range(n-k+1):
    sum_num = 0
    # 해당 구간 내의 원소의 합을 구한다.
    for j in range(i,i+k):
        sum_num += num[j]
    
    # 최댓값 구하기
    result = max(sum_num,result)

print(result)