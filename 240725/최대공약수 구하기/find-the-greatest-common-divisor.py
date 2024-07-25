n, m = tuple(map(int,input().split()))

def find(n,m):
    for i in range(n,0,-1):
        if n % i == 0 and m % i == 0:
            print(i)
            break

find(n,m)