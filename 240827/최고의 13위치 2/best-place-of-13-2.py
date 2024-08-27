n = int(input())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

result = 0

for i in range(n):
    for j in range(n):
        if in_range(i,j+1) and in_range(i,j+2):
            cury1 = j
            cnt = 0
            while(1):
                if arr[i][cury1] == 1:
                    cnt += 1
                if cury1 == j+2:
                    break
                cury1 += 1

            cnt_final = cnt
            for k in range(i+1,n):
                for l in range(n):
                    if in_range(k,l+1) and in_range(k,l+2):
                        cury2 = l
                        
                        while(1):
                            if arr[k][cury2] == 1:
                                cnt_final += 1
                            if cury2 == l+2:
                                break
                            cury2 += 1
            
            result = max(result,cnt_final)

print(result)