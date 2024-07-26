N = input()

def find_elem(k,M):
    for i in range(len(M)):
        if N[k+i] != M[i]:
            return False
    return True

M = input()
answer = -1
for k in range(len(N)-len(M)+1):
    if find_elem(k,M):
        answer = k

print(answer)