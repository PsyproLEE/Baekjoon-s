# 입력받기
import sys

input = sys.stdin.read
data = input().splitlines()

N = int(data[0])  # 점의 개수
points = []

# 점의 좌표를 입력받아 리스트에 추가
for i in range(1, N + 1):
    x, y = map(int, data[i].split())
    points.append((x, y))

# 점들을 정렬 (x좌표 기준, 같으면 y좌표 기준)
points.sort()

# 정렬된 결과 출력
for point in points:
    print(point[0], point[1])