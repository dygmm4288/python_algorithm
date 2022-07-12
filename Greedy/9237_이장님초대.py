import sys
stdin = sys.stdin.readline

N = int(stdin())
trees = list(map(int,stdin().split()))

trees.sort(reverse=True)
ret = 0
i = 1
for tree in trees :
    ret = max(ret,i+tree)
    i += 1
print(ret+1)