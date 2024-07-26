def check(a,b):
    for i in range(0,len(a)-len(b)+2):
        start = i
        for j in range(len(b)):
            if a[start] != b[j]:
                break
            start += 1
            if j == len(b)-1:
                return True
    return False

n1, n2 = tuple(map(int,input().split()))

a = list(map(int,input().split()))
b = list(map(int,input().split()))

if check(a,b):
    print("Yes")
else:
    print("No")