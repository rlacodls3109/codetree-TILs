n = int(input())

for i in range(n):
    for j in range(n):
        #(i+1)*(n-j)
        print((i+1)*(n-j),end=" ")
    print()