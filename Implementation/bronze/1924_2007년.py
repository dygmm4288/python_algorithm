import sys
readline = sys.stdin.readline

x,y = map(int,readline().split())

days = ['SUN','MON','TUE','WED','THU','FRI','SAT']
number_per_month = [31,28,31,30,31,30,31,31,30,31,30,31]

idx = 0
count = 0
while x > idx + 1 :
    count += number_per_month[idx]
    idx += 1
count += y
ret = days[count % 7]
print(ret)

