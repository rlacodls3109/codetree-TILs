n = int(input())
i = 0
cnt = 0
while(1):
    cnt += 1
    i += 1

    if (n / i) < 1:
        break
    else :
        n = n // i
print(cnt)