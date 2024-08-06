m1, d1, m2, d2 = tuple(map(int,input().split()))

# 각 날마다 달이 얼마나 있는지
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

'''
#1월 1일부터 며칠이 지났는지 계산하기 위한 변수 
start_days = 0
end_days = 0

#시작일부터 며칠인지 계산
for i in range(1,m1):
    start_days += num_of_days[i]

start_days += d1

#마지막날부터 며칠인지 계산
for j in range(1,m2):
    end_days += num_of_days[j]

end_days += d2
'''

def days(m,d):
    total_days = 0

    #1월부터 m-1월까지의 일을 다 더해준다
    for i in range(1,m):
        total_days += num_of_days[i]
    
    total_days += d

    return total_days

#흐른 날짜 계산

total_days = days(m2,d2) - days(m1,d1) + 1
print(total_days)