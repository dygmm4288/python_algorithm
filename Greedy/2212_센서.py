import sys
readline = sys.stdin.readline

n = int(readline())
k = int(readline())
if n <= k :
    print(0)
    quit(0)
sensors = list(map(int,readline().split()))
sensors.sort(reverse=True)
diff_sensors = []

for i in range(len(sensors)-1) :
    diff_sensors.append(sensors[i] - sensors[i+1])
diff_sensors.sort()
ret = 0
for i in range(len(sensors) - k) :
       ret += diff_sensors[i]
print(ret)