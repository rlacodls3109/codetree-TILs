def func(n,m):
    cnt = 1
    while(1):
        number = n * cnt
        if number % m == 0:
            print(number)
            break
        else :
            cnt += 1

arr = list(map(int,input().split()))
func(arr[0], arr[1])