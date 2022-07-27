import sys,collections
readline = sys.stdin.readline

n = int(readline())
numbers = [int(readline()) for _ in range(n)]
numbers.sort()

_sum = sum(numbers)
_mid = numbers[len(numbers)//2]
_range = numbers[-1] - numbers[0]
_most_common = collections.Counter(numbers).most_common(2)
print(round(_sum / n))
print(_mid)
if len(_most_common) > 1 :
    if _most_common[0][1] == _most_common[1][1] :
        print(_most_common[1][0])
    else :
        print(_most_common[0][0])
else :
    print(_most_common[0][0])
print(_range)







