import sys
readline = sys.stdin.readline

n = int(readline())
books = []
for _ in range(n):
    books.append(int(readline()))
ret = 0
next_number = n
for book in books[::-1]:
    if book == next_number :
        next_number -= 1
        ret += 1
print(n - ret)