import sys

INT_MIN = sys.maxsize

n = int(input())

people = list(map(int,input().split()))

dis_min = INT_MIN
for pos in range(n):
    total_dis = 0
    for each in range(n):
        total_dis += people[each] * abs(pos - each)
    if dis_min > total_dis:
        dis_min = total_dis

print(dis_min)