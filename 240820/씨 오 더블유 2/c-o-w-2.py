n = int(input())

given = input()

cnt = 0

# 모든 쌍을 다 잡아본다
for i in range(n):
    if given[i] == 'C':
        for j in range(i+1,n):
            if given[j] == 'O':
                for k in range(j+1,n):
                    if given[k] == 'W':
                        cnt += 1

print(cnt)