def max_n(n,A):
    if n == 1:
        return A[1]

    return max(max_n(n-1,A),A[n])

n = int(input())
A = [0]+list(map(int,input().split()))

print(max_n(n,A))