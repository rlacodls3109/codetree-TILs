import sys

n = int(input())

arr = list(map(int,input().split()))

min = sys.maxsize

for i in range(0,n):
    for j in range(i+1,n):
        sub = arr[i] - arr[j]
        
        if sub < 0:
            sub = 0-sub
        
        if sub < min:
            min = sub

print(min)