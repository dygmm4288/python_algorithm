import sys
readline = sys.stdin.readline
readline()
sum_round = lambda x : sum(list(map(abs,map(int,x))))
ret = lambda  : sum_round(readline().split())
print(ret() + ret())






    