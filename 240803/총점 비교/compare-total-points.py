class Student:
    def __init__(self,name,a,b,c):
        self.name = name
        self.a = a
        self.b = b
        self.c = c


n = int(input())

arr = [
    tuple(input().split())
    for _ in range(n)
]

students = [
    Student(name,int(a),int(b),int(c))
    for name,a,b,c in arr
]

students.sort(key = lambda x : x.a + x.b + x.c)

for S in students:
    print(S.name, S.a, S.b, S.c)