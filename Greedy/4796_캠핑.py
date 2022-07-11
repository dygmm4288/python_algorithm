i = 0
while True:
    # 연속하는 P일 중 L일동안만 캠핑 사용가능한데 사용 가능한 휴가가 V일
    L, P, V = map(int,input().split())
    if not L and not P and not V:
        break
    ret = ((V//P)*L) + min(L,V % P)
    print(f'Case {i}: {ret}')
    i += 1