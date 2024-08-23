def huang(x, y, p, q):
 for i in range(x,p):
  for j in range(y,q):
   arr[i][j] = 1

x1, y1, p1, q1 = map(int, input().split()) # 첫번째 사각형 정보
x2, y2, p2, q2 = map(int, input().split()) # 두번쨰 사각형 정보
x3, y3, p3, q3 = map(int, input().split()) # 세번째 사각형 정보
x4, y4, p4, q4 = map(int, input().split()) # 네번쨰 사각형 정보
arr = [ [0] * 101 for _ in range(101) ]

huang(x1, y1, p1, q1)
huang(x2, y2, p2, q2)
huang(x3, y3, p3, q3)
huang(x4, y4, p4, q4)

cnt = 0

for i in range(101):
 for j in range(101):
  if arr[i][j] == 1:
    cnt += 1

print(cnt)

# x1, y1, p1, q1 = map(int, input().split()) # 첫번째 사각형 정보
# x2, y2, p2, q2 = map(int, input().split()) # 두번쨰 사각형 정보
# x3, y3, p3, q3 = map(int, input().split()) # 세번째 사각형 정보
# x4, y4, p4, q4 = map(int, input().split()) # 네번쨰 사각형 정보

# arr = [0] * 100

# for i in range()