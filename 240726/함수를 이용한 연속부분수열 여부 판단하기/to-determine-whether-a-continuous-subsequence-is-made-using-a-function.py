# 함수 두개로 나누기!

def is_exist(n):
    for j in range(len(b)):
        if a[n+j] != b[j]:
            return False
    return True

def check(a,b):
    for i in range(len(a)-len(b)+1): 
        if is_exist(i):
            return True
    return False




n1, n2 = tuple(map(int,input().split()))

a = list(map(int,input().split()))
b = list(map(int,input().split()))

if check(a,b):
    print("Yes")
else:
    print("No")