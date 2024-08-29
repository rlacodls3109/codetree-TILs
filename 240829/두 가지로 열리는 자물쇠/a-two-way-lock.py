n = int(input())

a1, b1, c1 = tuple(map(int,input().split()))
a2, b2, c2 = tuple(map(int,input().split()))

result = 0

# 자리에 대한 거리가 2 이내인지 확인하는 함수
def dist_is_two(q,w):
    # 한 숫자가 8,9 일 경우에 확인하는 과정이 필요하다
    if (q == n and (w == 1 or w == 2)) or (w == n and (q == 1 or q == 2)):
        return True
    elif (q == n-1 and w == 1) or (w == n-1 and q == 1):
        return True
    else:
        return abs(q-w) <= 2

# 모든 자리를 1~n까지 탐색
for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            # 모든 자리에 대해 첫 번째 조합과 거리가 2이내라면
            if dist_is_two(i,a1) and dist_is_two(j,b1) and dist_is_two(k,c1):
                result += 1
            # 모든 자리에 대해 두 번째 조합과 거리가 2 이내라면
            # 둘 다 만족하는 경우는 하나로 생각하므로 elif
            elif dist_is_two(i,a2) and dist_is_two(j,b2) and dist_is_two(k,c2):
                result += 1
print(result)