arr = input().split()

a, b = int(arr[0]), int(arr[1])

result = 0

for i in range(a,b+1):
    if (1920 % i == 0) and (2880 % i == 0):
        result = 1

print(result)