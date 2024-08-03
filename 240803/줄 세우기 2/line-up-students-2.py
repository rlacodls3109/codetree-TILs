class Student:
    def __init__(self,h,w,n):
        self.h = h
        self.w = w
        self.n = n
    
N = int(input())

arr = [
    tuple(map(int,input().split()))
    for _ in range(N)
]

students = [
    Student(A[0],A[1],i+1)
    for i,A in enumerate(arr)
]

students.sort(key = lambda x : (x.h,-x.w))

for S in students:
    print(S.h,S.w,S.n)