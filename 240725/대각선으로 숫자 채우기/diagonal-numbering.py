n,m = tuple(map(int,input().split()))

arr_2d = [
    [0 for _ in range(m)]
    for _ in range(n)
]

cnt = 1
index_sum = 0
j = 0
i = 0
while(j < m and index_sum-j < n):
    current_j = j
    while(current_j >= 0 and index_sum-current_j < n):
        
        arr_2d[index_sum-current_j][current_j] = cnt
        cnt += 1
        current_j -= 1
    index_sum += 1
    if j < m-1:
        j += 1
   
    


for arr in arr_2d:
    for elem in arr:
        print(elem, end=" ")
    print()