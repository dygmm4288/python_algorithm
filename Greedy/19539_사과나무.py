import sys
readline = sys.stdin.readline

n = int(readline())
trees = list(map(int,readline().split()))
sum_of_tree = sum(trees)
sum_of_tree2 = sum(map(lambda x : x // 2,trees))
if sum_of_tree % 3 != 0 :
    print('NO')
else :
    if sum_of_tree2 >= sum_of_tree // 3:
        print('YES')
    else:
        print('NO')
    