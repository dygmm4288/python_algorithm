from_to, to_from = input().split()
ret = 1

# IF can divide 2 else -1
while int(from_to) < int(to_from):
    if int(to_from) % 2 == 0:
        to_from = str(int(to_from) // 2)
    elif to_from[len(to_from) -1] == '1':
        to_from = to_from[:-1]
    else: break
    ret += 1
if from_to == to_from: print(ret)
else: print(-1)
    

  
