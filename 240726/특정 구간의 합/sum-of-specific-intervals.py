n, m = tuple(map(int,input().split()))

A = [0] + list(map(int,input().split()))

def answer(a1, a2):
    sum = 0 
    for i in range(a1,a2+1):
        sum += A[i]
    return sum

for j in range(m):
    a1, a2 = tuple(map(int,input().split()))
    result = answer(a1, a2)
    print(result)