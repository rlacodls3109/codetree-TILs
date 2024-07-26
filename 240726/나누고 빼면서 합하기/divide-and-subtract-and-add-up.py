n, m = tuple(map(int,input().split()))
A = list(map(int,input().split()))

def modify_m(m):
    if m % 2 != 0:
        m -= 1
    else:
        m //= 2
    return m

def sum_A(m):
    sum = 0
    while(m >= 1):
        sum += A[m-1]
        m = modify_m(m)
    print(sum)

sum_A(m)