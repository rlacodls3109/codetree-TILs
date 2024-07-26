def is_yoon(Y):
    if Y % 4 != 0:
        return False
    
    if Y % 100 != 0:
        return True

    if Y % 400 != 0:
        return False
    
    return True

def last_day(Y,M):
    if M == 2:
        if is_yoon(Y):
            return 29
        return 28
    elif M == 4 or M == 6 or M == 9 or M == 11:
        return 30
    else:
        return 31
    
def is_exist(Y,M,D):
    if D <= last_day(Y,M):
        return True
    return False

def season(M):
    if M >=3 and M < 6 :
        return "Spring"
    elif M >= 6 and M < 9:
        return "Summer"
    elif M >= 9 and M < 12:
        return "Fall"
    else:
        return "Winter"

Y,M,D = tuple(map(int,input().split()))

if is_exist(Y,M,D):
    print(season(M))
else:
    print(-1)