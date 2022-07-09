S = int(input())
ret = 0
sum = 0
for n in range(1,S):
    sum += n
    ret += 1
    if(sum > S) :
        ret -= 1
        break;
print(ret)