full_str = input()
next_find_index = 0
find_word = ['U','C','P','C']
i = 0
while i < len(full_str) :
    if next_find_index > 3 : break
    if full_str[i] == find_word[next_find_index]:
        next_find_index += 1
    i += 1

if next_find_index == 4: print('I love UCPC')
else : print ('I hate UCPC')
    