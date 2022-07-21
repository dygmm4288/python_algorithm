import sys
readline = sys.stdin.readline

alpha = [-1] * 26

S = readline().strip()

for i in range(len(S)) :
    diff = ord(S[i]) - ord('a')
    if alpha[diff] == -1 :
        alpha[diff] = i
print(' '.join(map(str,alpha)))