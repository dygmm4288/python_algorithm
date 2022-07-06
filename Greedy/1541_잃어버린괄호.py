origin = input()
expression = origin.split('-')
minus = False
if origin[0] == '-' : minus = True

minus_list = []
for expr in expression:
    minus_list += [sum(map(int,expr.split('+')))]
ret = minus_list[0]
if minus : ret = -ret

for num in minus_list[1:]:
    ret -= num
print(ret)


