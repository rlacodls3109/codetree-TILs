n, m = tuple(map(int,input().split()))

result = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for i in range(m):
    r, c = tuple(map(int,input().split()))
    result[r-1][c-1] = i+1

for arr in result:
    for elem in arr:
        print(elem,end=" ")
    print()