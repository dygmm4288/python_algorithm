import sys
readline = sys.stdin.readline

n = int(readline())
sides = list(map(int,readline().split()))
def minimum(sides) :
    return lambda a,b : min(sides[a],sides[b])
#miminum_side
ms = minimum(sides)
#제일 작은 3개의 숫자
smallest_number = [ms(0,5),ms(1,4),ms(2,3)]
smallest_number.sort()
ret = 0
if n >= 2 :
    # 3side
    ret += 4 * sum(smallest_number)
    # 2side
    ret += (4 * (n -2) + 4 * (n-1)) * sum(smallest_number[:2])
    # 1side
    ret += (4 * (n-2)*(n-1) + (n-2) ** 2) * sum(smallest_number[:1])
else :
    sides.sort()
    ret += sum(sides[:5])
print(ret)