# 자기 방 번호를 플라스틱 문자로 문에 붙이렿 ㅏㄴ다
# 플라스틱 숫자를 한 세트를 판다
#한세트에는 0~ 9까지 숫자 필요한 세트의 개수 최솟값
# 6은 9로 사용 가능 9는 6으로 사용 가능
import sys
readline = sys.stdin.readline

n = readline().strip()
number = [0] * 10
for s in n : 
    num = int(s)
    if num == 6 or num == 9 :
        if num == 6 and number[9] < number[6]:
            number[9] += 1
        elif num == 9 and number[6] < number[9] :
            number[6] += 1
        else :
            number[num] += 1
    else :
        number[num] += 1
print(max(number))