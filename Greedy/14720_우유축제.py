N = int(input())
street = map(int,input().split())

prev = 2
ret = 0
for cur in street:
    if (prev + 1) % 3 == cur : 
        ret += 1
        prev = cur

print(ret)
    