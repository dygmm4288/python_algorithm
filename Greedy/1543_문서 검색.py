document = input()
word = input()
ret = 0
while True :
    index = document.find(word)
    if index == -1 : break
    ret += 1
    document = document[:index+len(word)]
print(ret)