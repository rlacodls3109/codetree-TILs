def answer(N):
    if N == 1:
        return 1
    
    return answer(N-1) + N

n = int(input())
print(answer(n))