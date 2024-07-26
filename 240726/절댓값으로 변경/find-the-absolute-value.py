n = int(input())
arr = list(map(int,input().split()))

def absolute_num(arr):
    for i in range(len(arr)):
        if arr[i] < 0 :
            arr[i] = -arr[i]

absolute_num(arr)

for elem in arr:
    print(elem, end= " ")