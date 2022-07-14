IMPOSSIBLE = "I'm Sorry Hansoo"

names = list(input())
names.sort()
dic = {}

def make(dic,odd) :
    ret = []
    for key in dic.keys():
        temp = key * (dic.get(key)//2)
        ret.append(temp)
    reverse_ret = ret[:]
    reverse_ret.reverse()
    if odd :
        ret.append(odd)
    return ''.join(ret + reverse_ret)

for name in names :
    if not name in dic :
        dic[name] = 0
    dic[name] = dic.get(name) + 1
# 팰린드롬이 되려면 
# 짝수 일 경우
if len(names) % 2 == 0:
    # 짝수 개로 모두 맞춰져 있어야 됨
    can = True
    for key in dic.keys():
        if dic.get(key) % 2 != 0 :
            can = False
            break
    # 모두 짝수 개가 아니라면
    if not can :
        print(IMPOSSIBLE)
    else :
        print(make(dic,False))
# 홀수 인 경우
elif len(names) % 2 != 0:
    # 1개의 홀수로 맞춰져 있어야 됨
    can = True
    odd_key = ''
    for key in dic.keys() :
        if dic.get(key) %2 != 0 and can and not odd_key :
            odd_key = key
        elif dic.get(key) %2 != 0 and odd_key:
            can = False
            break
    if not can :
        print(IMPOSSIBLE)
    else :
        dic[odd_key] = dic.get(odd_key) - 1
        print(make(dic,odd_key))
    
        