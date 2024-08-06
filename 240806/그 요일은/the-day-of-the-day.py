m1, d1, m2, d2 = tuple(map(int,input().split()))
A = input()

#1월 1일부터 며칠이 지났는 지 구하는 함수
def num_of_days(m,d):
    answer = 0

    days = [0,31,29,31,30,31,30,31,31,30,31,30,31]

    for i in range(1,m):
        answer += days[i]
    answer += d

    return answer

# 주어진 두 날짜의 차이를 구한다.
diff = num_of_days(m2,d2) - num_of_days(m1, d1)

# 배열로 각각의 요일을 저장. diff % 7를 인덱스로 가진다.
week = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

# A요일이 몇번 나오는지 구하기 위해 week.index(A)를 빼준다.
# 월요일을 기준으로 A요일이 며칠 차이나는 지를 week.index(A)를 통해 구할 수 있다.
# diff 값을 주어진 A요일을 기준으로 하도록 보정해야 함
diff -= week.index(A)

# 날짜의 차이를 7로 나누어 요일이 얼마나 나타났는 지 구한다.
answer = (diff // 7) + 1

print(answer)