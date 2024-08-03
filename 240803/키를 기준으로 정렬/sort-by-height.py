class Student:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

n = int(input())

arr = [
    tuple(input().split())
    for _ in range(n)
]

students = [
    Student(name,height,weight)
    for name,height,weight in arr
]

students.sort(key = lambda x: x.height)

for arr in students:
    print(arr.name, arr.height, arr.weight)