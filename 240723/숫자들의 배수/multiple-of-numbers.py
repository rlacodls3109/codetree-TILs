n = int(input())
arr = []
cnt = 0
cnt2 = 0

while(1):
    cnt += 1
    arr.append(n*cnt)
    if (n*cnt) % 5 == 0:
        cnt2 += 1
    if cnt2 == 2:
        break

for i in arr:
    print(i,end=" ")