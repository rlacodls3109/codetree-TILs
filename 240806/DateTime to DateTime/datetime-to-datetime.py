a, b, c = tuple(map(int,input().split()))

def answer(a,b,c):
    ## 11일 11시 11분 보다 앞서면
    if a < 11:
        return -1
    elif a == 11:
        if b < 11:
            return -1
        elif b == 11:
            if c < 11:
                return -1
        
    min_1111 = 11*60*24 + 11*60 + 11
    min_end = a*60*24 + b*60 + c
    
    return min_end - min_1111

print(answer(a,b,c))