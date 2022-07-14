import sys
readline = sys.stdin.readline

A,B,C,M = map(int,readline().split())

cur_time = 0
ret = 0
fatigue = 0
while cur_time < 24 :
    # time go on
    cur_time += 1
    # i can work
    if fatigue + A <= M :
        ret += 1
        fatigue += A
    # i cant work
    else :
        fatigue = max(0, fatigue - C)
        
print(ret * B)