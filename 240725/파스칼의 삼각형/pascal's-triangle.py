n = int(input())

triangle = [
    [0 for _ in range(i+1)]
    for i in range(n)
]

for i in range(n):
    triangle[i][0] = 1
    triangle[i][i] = 1

for i in range(2,n):
    for j in range(1,i):
        triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]


for arr in triangle:
    for elem in arr:
        print(elem,end=" ")
    print()