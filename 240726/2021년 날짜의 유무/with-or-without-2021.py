def is_exist_M(M):
    if M >= 1 and M <= 12:
        return True
    else:
        return False

def is_exist_D(M,D):
    if M <= 7:
        if M == 2:
            if D <= 28 and D >= 1:
                return True
        elif M % 2 == 0:
            if D <= 30 and D >= 1:
                return True
        else: 
            if D <= 31 and D >= 1:
                return True
    
    else:
        if M % 2 == 0:
            if D <= 31 and D >= 1:
                return True
        else :
            if D <= 31 and D >= 1:
                return True
    
    return False

M, D = tuple(map(int,input().split()))

if is_exist_M(M):
    if is_exist_D(M,D):
        print("Yes")
    else:
        print("No")
else:
    print("No")