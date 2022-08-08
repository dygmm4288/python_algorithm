
import sys, itertools
readline = sys.stdin.readline

n,m = map(int,readline().split())

home = []
chicken = dict()
for y in range(n) :
    for x,value in enumerate(readline().rstrip().split()) :
        if value == '1' :
            home.append([y,x])
        elif value == '2' :
            chicken[str(y*50+x)] = (y,x)

ret = sys.maxsize
combi = itertools.combinations

for i in range(1,m+1) :
    alive_chicken = list(combi(chicken,i))
    for alive in alive_chicken :
        city_distance = 0
        for h in home :
            r1,c1 = h
            cand = sys.maxsize
            for c in alive :
                r2,c2 = chicken[c]
                cand = min(cand, abs(r1-r2) + abs(c1-c2))
            city_distance += cand
        ret = min(ret,city_distance)
print(ret)