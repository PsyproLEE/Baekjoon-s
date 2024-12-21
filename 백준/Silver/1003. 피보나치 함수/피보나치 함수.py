import sys

dp = [[0, 0] for _ in range(41)]  # 최대 입력값 40 기준 (0 ~ 40)

dp[0] = [1, 0]
dp[1] = [0, 1]

for i in range(2, 41):
    dp[i][0] = dp[i - 1][0] + dp[i - 2][0]
    dp[i][1] = dp[i - 1][1] + dp[i - 2][1]

# 입력 처리
N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    num = int(sys.stdin.readline().rstrip())
    print(dp[num][0], dp[num][1])
