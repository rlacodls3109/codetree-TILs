n = int(input())
arr = list(map(int,input().split()))
tf = 'True'
max = -1
check = []
for i in range(0,len(arr)) :
    tf = 'True'
    if arr[i] in check:
        tf= 'False'
        continue
    if i+1 <= len(arr):
        for j in range(i+1,len(arr)) :
            if arr[i] == arr[j]:
                tf = 'False'
                check.append(arr[j])

        if tf == 'True' and arr[i] > max:
            max = arr[i]

print(max)