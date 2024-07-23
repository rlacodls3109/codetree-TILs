n = int(input())
arr = list(map(int,input().split()))
cnt = 0

for index,num in enumerate(arr):
    if num == 2:
        cnt += 1
    if cnt == 3:
        print(index+1)
        break