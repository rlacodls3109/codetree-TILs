class next_level:
    def __init__(self,id_="codetree",level="10"):
        self.id_=id_
        self.level=level

next_level1 = next_level()
print("user",next_level1.id_,"lv",next_level1.level)

a,b = tuple(input().split())
next_level1.id_ = a
next_level1.level = b

print("user",next_level1.id_,"lv",next_level1.level)