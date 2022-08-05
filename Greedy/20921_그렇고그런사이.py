import sys
readline = sys.stdin.readline

n,k = map(int,readline().split())

people = [i+1 for i in range(n)]

def swap(a,b) :
    people[a],people[b] = people[b],people[a]

for i in range(0,n) :
    if k == 0 : break
    for j in range(n-1,i,-1) :
        if k == 0 :
            break
        swap(j,j-1)
        k -= 1
print(' '.join(map(str,people)))
    