problem = input()

ans = 0

# 주어진 문자열 탐색
for i,ch in enumerate(problem):
    # 열린 괄호가 나오면
    if ch == '(':
        # 해당 위치의 다음부터 문자열의 끝까지 탐색
        for j in range(i+1,len(problem)):
            # 닫는 괄호가 나오면 count
            if problem[j] == ')':
                ans += 1

print(ans)