given = input()

cnt = 0
#연속하는 두 괄호가 모두 '('라면
#반복횟수는 len(given) - 1 이어야 한다.
for i in range(len(given)-1):
    if given[i] == '(' and given[i+1] =='(':
        #그 이후의 문자열 중 연속하는 ')' 가 있는지 찾아본다
        for j in range(i+2,len(given)-1):
            if given[j] == ')' and given[j+1] == ')':
                cnt += 1

print(cnt)