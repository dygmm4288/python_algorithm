alpha = ['a','b','c','d','e','f','g','h']
string = input()
y, x = alpha.index(string[0])+1, int(string[1])

dy = [-1,-1,1,1,-2,-2,2,2]
dx = [-2,2,-2,2,-1,1,-1,1]
count = 0
for i in range(len(dy)):
  ny = y + dy[i]
  nx = x + dx[i]
  if ny < 1 or ny > 8 or nx <1 or nx > 8 : continue

  count += 1

print(count)
  

input_data = input()
row = int(input_data[1])
column = int(input_data[0])) - int(ord('a')) + 1

steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)
