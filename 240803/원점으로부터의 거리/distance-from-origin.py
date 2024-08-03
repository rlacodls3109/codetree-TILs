n = int(input())

arr = [
    tuple(map(int,input().split()))
    for _ in range(n)
]

points = [
    (arr[0],arr[1],i+1)
    for i,arr in enumerate(arr)
]

points.sort(key = lambda x: abs(x[0])+abs(x[1]))

for P in points:
    print(P[2])