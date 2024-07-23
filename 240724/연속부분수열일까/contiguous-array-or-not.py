arr = list(map(int,input().split()))
n1, n2 = arr[0], arr[1]

A = list(map(int,input().split()))
B = list(map(int,input().split()))
result = 0
for i in range(len(A)):
    if A[i] == B[0] and len(A)-i >= len(B):
        for j in range(len(B)):
            if A[i+j] != B[j]:
                result = 'No'
                break
            else:
                result = 'Yes'
        if result == 'Yes':
            break

    else : 
        result = 'No'
    
print(result)