def one_to_n(n):
    if n == 0:
        return
    
    one_to_n(n-1)
    print(n,end=" ")

def n_to_one(n):
    if n == 0 :
        return
    
    print(n,end=" ")
    n_to_one(n-1)

N = int(input())
one_to_n(N)
print()
n_to_one(N)