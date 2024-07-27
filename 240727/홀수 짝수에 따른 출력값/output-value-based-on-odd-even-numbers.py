def answer(n):
    if n == 1 or n == 2:
        return n
    return answer(n-2) + n

n = int(input())
print(answer(n))