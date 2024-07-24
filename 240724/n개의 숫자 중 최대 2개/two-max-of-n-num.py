n = int(input())

arr = list(map(int,input().split()))
max_arr = []

while(1):
    max = arr[0]
    for i in arr:
        if max <= i:
            max = i

    max_arr.append(max)
    arr.remove(max)
    if len(arr) == 0:
        break
    
print(max_arr[0],max_arr[1])