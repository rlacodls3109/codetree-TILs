import sys

arr = list(map(int,input().split()))
max_gap = sys.maxsize
min_gap = sys.maxsize
min_num, max_num = 0,0

for i in arr:
    if i < 500 :
        gap = 500 - i
        if gap < min_gap:
            min_num = i
            min_gap = gap
    else :
        gap = i - 500
        if gap < max_gap:
            max_num = i
            max_gap = gap

print(min_num,max_num)