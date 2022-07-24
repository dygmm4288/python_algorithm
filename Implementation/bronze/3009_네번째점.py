import sys,collections
readline = sys.stdin.readline

x_count = collections.defaultdict(int)
y_count = collections.defaultdict(int)
for _ in range(3):
    x,y = map(int,readline().split())
    x_count[x] += 1
    y_count[y] += 1
def get(dic) :
    for key,value in dic.items() :
        if value == 1 :
            return key
        
ret = [get(x_count),get(y_count)]
print(' '.join(map(str,ret)))