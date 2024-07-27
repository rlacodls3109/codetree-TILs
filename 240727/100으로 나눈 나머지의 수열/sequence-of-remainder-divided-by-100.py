def answer(n):
    if n == 1:
        return 2
    if n == 2:
        return 4
    
    return ( answer(n-1)*answer(n-2) ) % 100

N = int(input())
print(answer(N))