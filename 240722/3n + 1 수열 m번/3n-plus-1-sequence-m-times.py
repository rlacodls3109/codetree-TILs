m = int(input())

for i in range(m):
    n = int(input())
    cnt = 0

    while(1):
        if n == 1:
            break
        if n % 2 == 0 :
            n = n // 2
        else :
            n = n * 3 + 1
        
        cnt += 1

        

    print(cnt)