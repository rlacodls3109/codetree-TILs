N, B = tuple(map(int,input().split()))

def chage_to_B(n,b):
    result = []
    while(1):
        if n < b:
            result.append(n)
            break
        else:
            result.append(n%b)
            n //= b
    
    return result

digits = chage_to_B(N,B)

for digit in digits[::-1]:
    print(digit,end="")