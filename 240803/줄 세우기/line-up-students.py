class Student:
    def __init__(self,h,w,k):
        self.h = h
        self.w = w
        self.k = k
    
N = int(input())
students = []

for i in range(N):
    x = tuple(map(int,input().split()))
    students.append(Student(x[0],x[1],i+1))

students.sort(key = lambda x : (-x.h,-x.w,x.k))

for S in students:
    print(S.h,S.w,S.k)