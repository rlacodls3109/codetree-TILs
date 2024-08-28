n = int(input())

a,b,c = tuple(map(int,input().split()))

def def_two(q,w):
    return abs(q-w) <= 2

result = n*n*n

for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            if not def_two(a,i) and not def_two(b,j) and not def_two(c,k):
                result -= 1

print(result)