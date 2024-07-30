n = int(input())
number = list(map(int,input().split()))

arr = []

for i in range(len(number)):
    arr.append(number[i])
    arr.sort()
    if (i+1) % 2 != 0:
        index = (1 + (i+1)) // 2
        print(arr[index-1],end=" ")