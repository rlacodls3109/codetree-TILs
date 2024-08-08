N, K, P, T = tuple(map(int,input().split()))

#감염유무 배열 감염되면 1 아니면 0
people = [0] * (N+1)
people[P] = 1

# 감염 횟수 배열
# 감염되면 +K, 감염시킬 때 마다 -1
inf_cnt = [0] * (N+1)
inf_cnt[P] += K

#감염 시키는 case들 입력 받기
case_arr =[
    list(map(int,input().split()))
    for _ in range(T)
]

# 시간 순으로 감염이 진행되어야 하므로 시간에 대하여 정렬
case_arr.sort(key= lambda x: x[0])

for case_ in case_arr:
    t, x, y = tuple(case_)
    # x,y 둘 다 감염되어 있다면 x,y 둘 다 감염횟수 감소
    if people[x] == 1 and people[y] == 1:
        inf_cnt[x] -= 1 if inf_cnt[x] > 0 else 0
        inf_cnt[y] -= 1 if inf_cnt[y] > 0 else 0
    
    # x가 감염되어 있고, 감염 횟수가 남아있다면
    # y감염 및 감염횟수 K번 추가, x의 감염횟수 1감소

    elif people[x] == 1 and inf_cnt[x] > 0:
        people[y] = 1
        inf_cnt[y] += K
        inf_cnt[x] -= 1 if inf_cnt[x] > 0 else 0
    
    # y가 감염되어 있고, 감염 횟수가 남아있다면
    # x감염 및 감염횟수 K번 추가, y의 감염횟수 1감소
    elif people[y] == 1 and inf_cnt[y] > 0:
        people[x] = 1
        inf_cnt[x] += K
        inf_cnt[y] -= 1 

    # 둘 다 감염되지 않은 경우
    else:
        continue

for person in people[1::]:
    print(person,end="")