n = int(input())

arr = list(map(int,input().split()))
new = []
for i in arr:
    if i % 2 == 0:
        new.append(i)
    
for j in new[::-1]:
    print(j, end=" ")