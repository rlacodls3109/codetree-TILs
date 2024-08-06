m1, d1, m2, d2 = tuple(map(int,input().split()))
w = input()

#1월 1일부터 며칠이 지났는 지 구하는 함수
def num_of_days(m,d):
    answer = 0

    days = [0,31,29,31,30,31,30,31,31,30,31,30,31]

    for i in range(1,m):
        answer += days[i]
    answer += d

    return answer

diff = num_of_days(m2,d2) - num_of_days(m1, d1)
week = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

week_count = diff - week.index(w)

answer = ( week_count // 7) + 1

print(answer)