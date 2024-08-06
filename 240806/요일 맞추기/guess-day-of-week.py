# 2011년 1월 1일부터 며칠이 지났는 지 구하는 함수
def num_of_days(m,d):

    days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

    answer = 0
    #2011년 1월 1일 부터 며칠이 지났는 지
    for i in range(1,m):
        answer += days[i]
    answer += d

    return answer

# 날짜의 차이로 요일 구하는 함수
def find_week(k):
    # 날짜의 차이에 따른 요일을 배열로 지정
    week = ["Mon","Sun","Sat","Fri","Thu","Wed","Tue"]
    return week[k]

m1,d1, m2, d2 = tuple(map(int,input().split()))

# 기준이 되는 날짜에서 요일을 찾을 날짜를 뺀다
diff = num_of_days(m1, d1) - num_of_days(m2, d2)

# diff를 7로 나눈 나머지에 대해 요일을 찾는다.
week = find_week(diff % 7)
print(week)