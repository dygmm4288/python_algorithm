# 책의 개수 n과 박스 최대 무게 m
# 차례대로 박스에 넣을 수 밖에 없다
import sys
readline = sys.stdin.readline

n,m = map(int,readline().split())
if n == 0 :
    print(0)
    sys.exit(0)
books = list(map(int,readline().split()))

ret = 1
#차례대로 박스에 넣는다
in_box = 0
for book in books :
    in_box += book
    #박스에 넣었는데 박스 최대 무게보다커지면 그 물건은 담을 수 없다
    #박스를 한개 추가해야 한다
    if in_box > m :
        ret += 1
        #추가한 박스에 다시 책을 넣는다
        in_box = book
print(ret)