def answer(string):
    cnt = 0
    for i in range(len(string)-1):
        for j in range(i+1,len(string)):
            if string[i] != string[j]:
                cnt += 1
        if cnt >= 2:
            return True
    return False


A = input()
if answer(A):
    print("Yes")
else:
    print("No")