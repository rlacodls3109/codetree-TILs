arr = list(map(int,input().split()))
n, m = arr[0], arr[1]

arr_2d = [
    [0 for _ in range(m)]
    for _ in range(n)
]

for i in range(n):
    for j in range(m):
        arr_2d[i][j] += 1

for array in arr_2d:
    for elem in array:
        print(elem,end=" ")
    print()