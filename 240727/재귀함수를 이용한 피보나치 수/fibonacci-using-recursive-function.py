def pivo(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    
    return pivo(n-2) + pivo(n-1)

n = int(input())
print(pivo(n))