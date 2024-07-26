def answer(N):
    if N == 0:
        return
    
    print(N)
    answer(N-1)
    print(N)

n = int(input())
answer(n)