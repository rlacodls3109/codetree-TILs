N, M, K = tuple(map(int,input().split()))

check_student = [0] * (N+1)
student_payturn = [-1] * (N+1)

pay_turn = 1

for _ in range(M):
    student_num = int(input())
    check_student[student_num] += 1

    if check_student[student_num] == K:
        student_payturn[pay_turn] = student_num
        pay_turn += 1

print(student_payturn[1])