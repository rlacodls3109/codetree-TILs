n = int(input())
i = 0
while(1):
    i += 1

    if (n / i) <= 1:
        break
    else :
        n = n // i
print(i)