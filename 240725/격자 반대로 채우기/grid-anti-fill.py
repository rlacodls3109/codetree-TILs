n = int(input())

cnt = 1

arr_2d =[
    [0 for _ in range(n)]
    for _ in range(n)
]

for j in range(n-1,-1,-1):
    if (n-1-j) % 2 == 0:
        for i in range(n-1,-1,-1):
            arr_2d[i][j] = cnt
            cnt += 1
    else :
        for i in range(n):
            arr_2d[i][j] = cnt
            cnt += 1

for arr in arr_2d:
    for elem in arr:
        print(elem,end=" ")
    print()