import sys
readline = sys.stdin.readline

# S 를 T로 만들기 위해서는
# 문자열 뒤에 A를 추가하거나 -> 문자열 맨 뒤가 A이다
# 문자열을 뒤집고 뒤에 B를 추가한다 -> 문자열 맨 뒤가 B이다

S = readline().strip()
T = readline().strip()

while T != S and len(S) <= len(T) :
    if T[-1] == 'B' : 
        T = T[0:-1][::-1]
    else :
        T = T[:-1]
if T == S : print(1)
else :print(0)