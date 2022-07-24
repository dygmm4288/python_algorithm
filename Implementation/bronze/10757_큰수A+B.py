import sys
readline = sys.stdin.readline

a,b = readline().strip().split()
a = a[::-1]
b = b[::-1]
a_digit = len(a)
b_digit = len(b)

idx = 0 
ret = 0

for i in range(min(a_digit,b_digit)) :
    ret += int(a[i]) * (10 ** i)
    ret += int(b[i]) * (10 ** i)
    idx += 1
for i in range(idx,max(a_digit,b_digit)) :
    if a_digit > idx :
      ret += int(a[i]) * (10 ** (i))
    if b_digit > idx :
      ret += int(b[i]) * (10 ** (i))
print(ret)


