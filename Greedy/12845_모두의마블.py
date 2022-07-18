import sys
readline = sys.stdin.readline

#순서가 매겨진 여러 장의 카드
# 각각의 카드는 저마다 레벨이 있다
#카드 A에 카드B를 붙이는 조건은
# 1. 두 카드는 인접한 카드여야 한다
# 2. 업그레이드 된 카드 A의 레벨은 변하지 않는다
# 카드합성시마다 두카드레벨의 합만큼 골드를 받는다 최대 골드
n = int(readline())
cards = list(map(int,readline().split()))
MAX = max(cards)
SUM = sum(cards)
#계속해서 더 높은 쪽을 계산하면 되지 않나..
ret = MAX*(n-2) + SUM
print(ret)


