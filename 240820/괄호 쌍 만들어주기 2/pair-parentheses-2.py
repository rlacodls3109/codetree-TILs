given = input()

cnt = 0
for i in range(len(given)-1):
    if given[i] == '(' and given[i+1] =='(':
        for j in range(i+2,len(given)-1):
            if given[j] == ')' and given[j+1] == ')':
                cnt += 1

print(cnt)