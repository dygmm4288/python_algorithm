import sys
readline = sys.stdin.readline

def calc_partial_sum(li) :
    ret = [li[0]]
    for item in li[1:]:
        ret.append(ret[-1] + item)
    return ret

N = int(readline())  
honey = list(map(int,readline().split()))
ret = 0
#partial sum
p_sum = calc_partial_sum(honey)
#reverse partial sum
rp_sum = calc_partial_sum(honey[::-1])

#fixed at both ends
#left bees, right hive
left_bees_right_hive = 2 * p_sum[N-1] - p_sum[0]
right_bees_left_hive = 2 * rp_sum[N-1] - rp_sum[0]
for i in range(1,N) :
    ret = max(
        ret,
        left_bees_right_hive - p_sum[i] - honey[i],
        right_bees_left_hive - rp_sum[i] - honey[N-i-1]
    )
    if i >= 1 and i<= N - 2 :
        ret = max(
            ret,
            p_sum[i] - p_sum[0] +
            rp_sum[N-i-1] - rp_sum[0]
        )
print(ret)