import sys

# sys.stdin을 사용해 EOF까지 입력받기
for line in sys.stdin:
    # 입력받은 줄을 공백을 기준으로 나누고, 정수로 변환
    A, B = map(int, line.split())
    # A + B 출력
    print(A + B)