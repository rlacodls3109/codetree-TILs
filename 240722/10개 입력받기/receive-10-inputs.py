sum = 0
cnt = 0

arr = list(map(int,input().split()))

for i in arr:
    if i == 0:
        break
    cnt += 1
    sum += i

avg = sum / cnt
print(sum, f"{avg:.1f}")