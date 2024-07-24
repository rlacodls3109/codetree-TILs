arr = [
    list(map(int,input().split()))
    for n in range(4)
]

for array in arr:
    print(sum(array))