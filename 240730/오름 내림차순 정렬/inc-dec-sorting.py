n = int(input())
arr = list(map(int,input().split()))

arr.sort()
for elem in arr:
    print(elem,end=" ")
print()
arr.sort(reverse=True)
for elem in arr:
    print(elem,end=" ")