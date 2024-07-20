arr = input().split()

b, a = int(arr[0]), int(arr[1])

for i in range(b,a-1,-1):
    if i % 2 != 0:
        print(i, end = " ")