arr = input().split()

a,b = int(arr[0]), int(arr[1])

for i in range(1,10):
    for j in range(b,a-1,-1):
        if j % 2 == 0:
            print(f"{j} * {i} = {j*i}", end=" ")

            if j != a and j != a+1:
                print("/", end=" ")
    print()