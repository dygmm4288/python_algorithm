import sys
readline = sys.stdin.readline

T = int(readline())
for _ in range(T) :
    a = readline().strip()
    n = len(a)
    # 현재 a보다 큰 숫자를 만들기 위해서는
    # 뒤에서부터 순회하면서 a[i] > a[i-1]인 point를 찾아야 한다
    point = -1
    for i in range(n-1,0,-1) :
        if a[i] > a[i-1] :
            point = i-1
            break
    if point == -1 :
        print('BIGGEST')
        continue
    else :
        # 큰 수 중 가장 작은 수를 찾기 위해서는
        # point를 기점으로 a[point]보다 처음으로 큰 숫자를 찾아야 한다
        # 찾은 큰 숫자는 point 자리에 가야하기 때문에 맨 앞으로 빼준다
        # 이때, a[point+1] > a[point]인 지점을 찾았기 때문에
        # 항상 큰 숫자는 한개 이상 있다.
        b = list(a[point:])
        b.sort()
        ret = list(a[:point])
        for i in range(len(b)) :
            if a[point] < b[i] :
                ret += [b.pop(i)]
                break
        ret += b
        print(''.join(map(str,ret)))
        
        
        