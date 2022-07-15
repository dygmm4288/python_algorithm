import sys
readline = sys.stdin.readline

n = int(readline())

#to int
origin_state = list(map(int,readline().strip()))
next_state = list(map(int,readline().strip()))

def change(value) :
    return (value + 1) % 2
def solve(origin_state,next_state,first) :
    ret = 0
    if first == 1 :
        origin_state[0] = change(origin_state[0])
        origin_state[1] = change(origin_state[1])
        ret = 1
    for i in range(1,len(origin_state)) :
        if origin_state[i-1] != next_state[i-1] :
            origin_state[i-1] = change(origin_state[i-1])
            origin_state[i] = change(origin_state[i])
            if i + 1 < n : 
                    origin_state[i+1] = change(origin_state[i+1])
            ret += 1
    return ret if origin_state == next_state else 987654321
ret = min(
  solve(origin_state[:],next_state,0),
  solve(origin_state[:],next_state,1)
)
print(ret if ret != 987654321 else -1)
        