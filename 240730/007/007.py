class secret:
    def __init__(self,key,place,time):
        self.key = key
        self.place = place
        self.time = time


code, place, time = tuple(input().split())

secret1 = secret(code,place,time)

print("secret code :", secret1.key)
print("meeting point :", secret1.place)
print("time :", secret1.time)