class Bomb:
    def __init__(self,code,color,sec):
        self.code = code
        self.color = color
        self.sec = sec

a, b, c = tuple(input().split())
c = int(c)

bomb1 = Bomb(a,b,c)

print("code :", bomb1.code)
print("color :", bomb1.color)
print("second :", bomb1.sec)