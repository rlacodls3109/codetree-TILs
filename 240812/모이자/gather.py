import sys

# 최솟값을 시스템상 최댓값으로 설정
INT_MIN = sys.maxsize

n = int(input())

people = list(map(int,input().split()))

dis_min = INT_MIN

#pos 번 집으로 모였을 때의 합을 구함
for pos in range(n):
    total_dis = 0
    for each in range(n):
        total_dis += people[each] * abs(pos - each)
    
    # 가능한 거리의 합 중 최소값을 구함
    dis_min = min(dis_min,total_dis)


print(dis_min)