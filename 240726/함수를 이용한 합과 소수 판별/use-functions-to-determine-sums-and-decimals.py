def is_sosu(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    
    return True

def check_sum(n):
    sum = 0
    while (n != 0):
        sum +=  n%10
        n = n // 10
    
    if sum % 2 == 0:
        return True
    else:
        return False

a, b = tuple(map(int,input().split()))

cnt = 0

for k in range(a,b+1):
    if is_sosu(k) and check_sum(k):
        cnt += 1
    
print(cnt)