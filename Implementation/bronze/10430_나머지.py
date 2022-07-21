import sys
readline = sys.stdin.readline

a,b,c = map(int,readline().split())

print((a+b) % c)
print(((a%c) + (b%c)) % c)
print((a*b) % c)
print(((a%c) * (b%c)) % c)