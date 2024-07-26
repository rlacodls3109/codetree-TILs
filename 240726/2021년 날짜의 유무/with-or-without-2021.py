'''
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
'''

def last_d(M):
    day = 0
    if M == 2:
        day = 28
    elif M == 4 or M == 6 or M == 9 or M == 11:
        day = 30
    else :
        day = 31
    return day

def is_exist(M,D):
    if M <= 12 and D <= last_d(M):
        return True
    else:
        return False

M, D = tuple(map(int,input().split()))

if is_exist(M,D):
    print("Yes")
else:
    print("No")