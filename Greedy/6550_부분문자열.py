import sys
readline = sys.stdin.readline

while True:
    temp = readline().strip()
    if not temp :
        break
    s, t = temp.split()
    
    s_index = 0
    for t_sub in t :
        if s_index == len(s) : break
        if s[s_index] == t_sub :
            s_index += 1
    print('Yes' if s_index == len(s) else 'No')