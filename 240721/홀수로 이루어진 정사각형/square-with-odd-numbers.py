n = int(input())

start = 11
for i in range(n):
    for j in range(n):
        print(start+(2*j), end=" ")
    start += 2
    print()