n = int(input())
arr = list(map(int,input().split()))
pos = n
current_pos = -1
while(1): 
    max = -1
    for i in range(0,pos):
        if max < arr[i]:
            max = arr[i]
            current_pos = i
    pos = current_pos
    print(pos+1,end=" ")
    if pos == 0:
        break