import sys

MIN_INT = sys.maxsize

N = int(input())

#각자 방에 몇 명이 들어가야 하는 지에 대한 리스트 
arr = [
    int(input())
    for _ in range(N)
]

ans = MIN_INT

#i번째 방에서 시작할 경우에 대해 탐색
for i in range(N):
    total_dist = 0
    #첫번째 방부터 마지막 방까지 순회하며
    for j in range(N):
        # 사람의 수와 거리를 곱해 이동 거리를 구한다.
        total_dist += arr[(i+j) % N] * j
    
    # 최소거리 구하기
    ans = min(ans,total_dist)

print(ans)