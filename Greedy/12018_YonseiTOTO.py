import sys
readline = sys.stdin.readline

n, m = map(int,readline().split())

def calc_min_mileage(p,l,students) :
    students.sort()
    if p < l :
        return 1
    else :
        return students[-l]

subjects = []
# append min mileage for subjects
for _ in range(n):
    p, l = map(int,readline().split())
    students = list(map(int,readline().split()))
    subjects.append(calc_min_mileage(p,l,students))

subjects.sort()

ret = 0
for subject in subjects :
    if subject <= m :
        m -= subject
        ret += 1
print(ret)
    