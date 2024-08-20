import sys

MAX_SIZE = -sys.maxsize

n = int(input())

arr = list(map(int,input().split()))

ans = MAX_SIZE

# 완전탐색 진행
for i in range(n):
    for j in range(i+1,n):
        # 만약 i와 j가 인접한 인덱스일 경우에는 진행하지 않는다.
        if j-i != 1:
            cal  = arr[i] + arr[j]
            ans = max(ans,cal)

print(ans)