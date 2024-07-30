import sys

class Codename:
    def __init__(self,name,score):
        self.name = name
        self.score = score
    

agents = []
for _ in range(5):
    name, score = tuple(input().split())
    score = int(score)
    agents.append(Codename(name,score))

min = sys.maxsize
idx = 0
for i in range(5):
    agent = agents[i]
    if min > agent.score:
        min = agent.score
        idx = i

print(agents[idx].name,agents[idx].score)