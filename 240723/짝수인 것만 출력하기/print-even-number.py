n = int(input())
arr = list(map(int,input().split()))

new = [elem for elem in arr if elem % 2 ==0]

for i in new:
    print(i, end=" ")