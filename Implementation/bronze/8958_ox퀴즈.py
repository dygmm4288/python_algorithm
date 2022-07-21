import sys
readline = sys.stdin.readline

for _ in range(int(readline())) :
    ox = readline().strip()
    ret = 0
    for i in range(len(ox)) :
        cnt = 0
        for value in ox[:i+1][::-1]:
            if value == 'X':
                break
            cnt +=1
        ret += cnt
    print(ret)