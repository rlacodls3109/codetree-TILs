arr = list(map(int,input().split()))

n,q = arr[0], arr[1]

array = list(map(int,input().split()))
for i in range(q):
    que = list(map(int,input().split()))
    if que[0] == 1:
        print(array[que[1]-1])
    
    elif que[0] == 2:
        if que[1] in array:
            index = array.index(que[1]) + 1
        else:
            index = 0
        print(index)
    
    elif que[0] == 3:
        for j in array[que[1]-1:que[2]:]:
            print(j,end=" ")
        print()