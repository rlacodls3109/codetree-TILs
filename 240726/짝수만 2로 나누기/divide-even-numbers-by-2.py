def even_divide(array):
    for i in range(len(array)):
        if array[i] % 2 == 0:
            array[i] = array[i] // 2
    

n = int(input())
arr = list(map(int,input().split()))

even_divide(arr)

for elem in arr:
    print(elem, end=" ")