m1, d1, m2, d2 = tuple(map(int,input().split()))
week = input()
def num_of_days(m,d):
    answer = 0

    days = [0,31,29,31,30,31,30,31,31,30,31,30,31]

    for i in range(1,m):
        answer += days[i]
    answer += d

    return answer

diff = num_of_days(m2,d2) - num_of_days(m1, d1)

count = (diff // 7) + 1

print(count)