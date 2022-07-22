import sys,collections
readline = sys.stdin.readline

string = readline().strip().upper()
count = collections.defaultdict(int)
MAX = 0
for s in string :
    count[s] += 1
    if MAX < count[s] : 
            MAX = count[s]
ret = ''
for key,value in count.items() :
    if value == MAX and ret == '':
        ret = key
    elif value == MAX and ret != '' :
        ret = '?'
print(ret)