def answer(string):
    cnt = 0
    for i in range(len(string)-1):
        for j in range(i+1,len(string)):
            if string[i] != string[j]:
                cnt += 1
        if cnt >= 2:
            return True
    return False

'''
# 코드 간소화
# 서로다른 알파벳이 한번이라도 나오면 true를 리턴한다.
# 즉, 문자열의 맨 첫 문자와 나머지 문자를 비교해서 다른게 나오면 바로 종료하면 된다.

for i in range(1,len(string)):
    if string[i] != string[0]:
        return True
    return False
'''

A = input()
if answer(A):
    print("Yes")
else:
    print("No")