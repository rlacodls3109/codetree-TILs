arr = input().split()
start, end = int(arr[0]), int(arr[1])
cnt1 = 0
cnt2 = 0
for i in range(start,end+1):
    cnt1 = 0
    for j in range(1, end+1):
        if i % j == 0:
            cnt1 += 1
    if cnt1 == 3:
        cnt2 += 1

print(cnt2)