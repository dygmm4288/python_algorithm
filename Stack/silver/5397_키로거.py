import sys
readline = sys.stdin.readline

T = int(readline())

for _ in range(T) :
    L = readline().rstrip()
    left = []
    right = []
    for s in L :
        # 백스페이스를 입력하면 커서의 바로 앞에 글자가 존재한다면 지운다
        if s == '-' and left :
            left.pop()
            continue
        # 화살표의 입력은 <와 >로 주어진다
        if s == '<' and left :
            right.append(left.pop())
            continue
        if s == '>' and right :
            left.append(right.pop()) 
            continue
        if s != '>' and s != '<' and s != '-' :
            left.append(s)
    print(''.join(left) + ''.join(right[::-1]))
        
    