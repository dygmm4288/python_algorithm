import sys

readline = sys.stdin.readline

dial = [
    2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9,
    9
]
diff = lambda x: ord(x) - ord('A')

words = readline().strip()
ret = len(words)
for word in words:
    ret += dial[diff(word)]

print(ret)
