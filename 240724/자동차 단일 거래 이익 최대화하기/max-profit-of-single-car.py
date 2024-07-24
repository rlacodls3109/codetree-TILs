n = int(input())
arr = list(map(int,input().split()))

max = 0
for i in range(0,len(arr)):
    if i+1 < len(arr):
        for j in range(i+1,len(arr)):
            if arr[j]>arr[i]:
                rest = arr[j]-arr[i]
                if rest > max:
                    max = rest

print(max)