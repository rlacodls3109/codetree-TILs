def answer(N):
    if N == 0:
        return
    
    print(N,end=" ")
    answer(N-1)
    print(N,end=" ")

n = int(input())
answer(n)