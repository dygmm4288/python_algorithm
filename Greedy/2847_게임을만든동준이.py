import sys
readline = sys.stdin.readline

N = int(readline())
levels = [0] * N
# input data
for i in range(N):
    levels[i] = int(readline())
# reverse list
levels.reverse()

ret = 0
# 0 to n -1
for i in range(len(levels) - 1):
    hard_level = levels[i]
    easy_level = levels[i+1]
    level_diff = easy_level - hard_level
    # it means that easy_level is higher than hard_level
    if level_diff >= 0 : 
        levels[i+1] = easy_level - (level_diff + 1)
        ret += level_diff + 1
    
print(ret)
        
    