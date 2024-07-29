def answer(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return answer(n//3) + answer(n-1)

n = int(input())
print(answer(n))