'''
이게 그러니까 왼쪽 혹은 오른쪽으로 모으는 것이 목푱니데
총 4가지가 있다 
빨간 공을 왼쪽 혹은 오른쪽
파란공을 왼쪽 혹은 오른쪽

연속된 것들은 모두 뛸 수 있다
그러면 양 끝 쪽에서 연속된 공을 제외하고는 모두 건너뛰어야 함

건너뛰는 순간 연속되지 않은 다른 공들은 연속적으로 변하게 됨으로
한번에 건너뛸 수 있다


'''
import sys
readline = sys.stdin.readline

N = int(readline())
balls = readline().strip()

redball_count = 0
blueball_count = 0
left_redball_count = 0
right_redball_count = 0
left_blueball_count = 0
right_blueball_count = 0
# count all,consecutive balls on the left
for ball in balls :
  if ball == 'R' :
      redball_count +=1
  if ball == 'B' :
      blueball_count += 1
  # 둘 중 하나라도 0이면 한가지 밖에 안나옴
  if redball_count != 0 or blueball_count != 0 :
      if redball_count == 0 :
         left_blueball_count = blueball_count
      elif blueball_count == 0 :
         left_redball_count = redball_count
# count consecutive balls on the right
for ball in balls[::-1]:
  if ball == 'R' :
      if right_blueball_count == 0 :
          right_redball_count += 1
      else : break
  if ball == 'B' :
      if right_redball_count == 0 :
          right_blueball_count += 1
      else : break

ret = min(
  redball_count - left_redball_count,
  redball_count - right_redball_count,
  blueball_count - left_blueball_count,
  blueball_count - right_blueball_count
)
print(ret)