import sys

n,h,t = tuple(map(int,input().split()))

arr = list(map(int,input().split()))

result_min = sys.maxsize

# i는 탐색할 구간의 시작 위치
for i in range(n-t+1):
    cost = 0
    # 구간 탐색하며 비용 구하기
    for j in range(i,i+t):
        cost += abs(h-arr[j])
    # 최솟값 갱신
    result_min = min(cost,result_min)

print(result_min)