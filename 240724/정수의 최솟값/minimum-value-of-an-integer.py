def minimum(a,b,c):
    min = a
    if b < min:
        min = b
    if c < min:
        min = c
    return min

arr = list(map(int,input().split()))
a, b, c = arr[0], arr[1], arr[2]

min = minimum(a,b,c)

print(min)