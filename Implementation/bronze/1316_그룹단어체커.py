import sys,collections
readline = sys.stdin.readline

def is_group_word(word) :
    count = collections.defaultdict(int)
    count[word[0]] += 1
    for i in range(1,len(word)) :
        if word[i] == word[i-1] :
            continue
        elif word[i] != word[i-1] and count[word[i]] != 0:
            return False
        else :
            count[word[i]] += 1
    return True
                
            

n = int(readline())
words = [readline().strip() for _ in range(n)]
ret = 0
for word in words :
    if is_group_word(word) :
        ret += 1
print(ret)