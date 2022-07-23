#호텔 정문으로부터 걷는 거리가 가장 짧도록 방을 배정하는 프로그램 작성
import sys
readline = sys.stdin.readline

for _ in range(int(readline())) :
    h,w,n = map(int,readline().split())
    if n % h == 0 :
        yy = h
        xx = n // h
    else :
        yy = n % h
        xx = (n // h) + 1
    if xx < 10 : xx = '0' + str(xx)
    print(str(yy) + str(xx))