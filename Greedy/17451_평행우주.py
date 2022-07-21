import sys
readline = sys.stdin.readline

n = int(readline())
planets = list(map(int,readline().split()))[::-1]

ret = 0
for planet in planets :
    if ret < planet :
        ret = planet
    elif ret > planet :
        # indivisible
        if ret % planet :
          ret = (ret//planet+1) * planet
print(ret)