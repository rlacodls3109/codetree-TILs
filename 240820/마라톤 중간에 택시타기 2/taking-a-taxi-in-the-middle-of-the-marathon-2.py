import sys

MIN_INT = sys.maxsize

# 택시거리 구하는 함수
def cal_Mdist(A,B):
    return abs(A[0]-B[0]) + abs(A[1]-B[1])

N = int(input())

# 각 체크포인트의 x,y좌표 저장하는 2차원 리스트
check_point = [
    list(map(int,input().split()))
    for _ in range(N)
]

ans = MIN_INT


for i in range(N): 
    # 첫번째 지점과 마지막 지점은 건너뛰지 않음
    if i !=0 or i != N-1: 
        
        # 첫번째 지점부터 시작
        start_point = check_point[0]
        total_distance = 0
        for index,point in enumerate(check_point):
            # i번째 체크포인트는 건너뛴다
            if index != i:
                #지점 간의 거리 구하기
                total_distance += cal_Mdist(start_point,point)
                # start_point 를 방금 지난 체크포인트로 바꾼다
                start_point = point
    
        # 최소 거리 구하기
        ans = min(ans,total_distance)

print(ans)