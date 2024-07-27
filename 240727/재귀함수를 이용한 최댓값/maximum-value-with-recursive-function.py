def max_n(n,A):
    if n == 1:
        return A[1]
    a = max_n(n-1,A)
    if a < A[n]:
        return A[n]
    else:
        return a

n = int(input())
A = [0]+list(map(int,input().split()))

print(max_n(n,A))