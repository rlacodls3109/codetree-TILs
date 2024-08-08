N, M, K = tuple(map(int,input().split()))

# 학생의 벌칙 횟수 셀 배열
check_student = [0] * (N+1)

# 벌금 내는 순서대로 번호를 넣기 위한 배열
student_payturn = []


for _ in range(M):
    student_num = int(input())
    #벌칙 횟수를 배열에 저장
    check_student[student_num] += 1

    # K번 이상 벌칙을 받은 사람 번호가 student_payturn 배열에 저장된다.
    if check_student[student_num] == K:
        student_payturn.append(student_num)

# 벌금 내는 순서의 배열이 비어있으면 -1, 아니라면 맨 첫번째 사람의 번호를 출력한다.
ans = -1 if len(student_payturn) == 0 else student_payturn[0]  

print(ans)