import sys
readline = sys.stdin.readline

for i in range(int(readline())) :
    a,b = map(int,readline().split())
    print(f'Case #{i+1}: {a+b}')