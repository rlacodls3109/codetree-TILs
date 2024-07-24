n = int(input())

arr_2d = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for i in range(n):
    for j in range(n):
        arr_2d[i][j] = (i+1) + n*j

for arr in arr_2d:
    for elem in arr:
        print(elem,end=" ")
    print()