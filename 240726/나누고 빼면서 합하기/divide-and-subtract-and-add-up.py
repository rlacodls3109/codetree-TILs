n, m = tuple(map(int,input().split()))
A = list(map(int,input().split()))

# m을 전역변수로 활용하면 더 효율적임!
def answer():
    global m
    sum = 0
    while m > 0:
        sum += A[m-1]

        if m % 2 == 0:
            m //= 2
        else:
            m -= 1
    return sum

print(answer())

'''
def modify_m():
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
'''