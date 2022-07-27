import sys
readline = sys.stdin.readline

alpha = [0] * 26

S = readline().strip()
for s in S :
    alpha[ord(s) - ord('a')] += 1
print(' '.join(map(str,alpha)))