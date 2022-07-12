N = int(input())

sits = '*' + input()

sits = sits.replace('S','S*')
sits = sits.replace('LL','LL*')

print(min(sits.count('*'),N))