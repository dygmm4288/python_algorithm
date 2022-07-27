import sys
readline = sys.stdin.readline

n = int(readline())

for i in range(n):
  print(' '*i + '*'*((2*n)-(2*i) -1 ))
    
        
  