import sys

N = int(sys.stdin.readline().rstrip())
P = sorted(map(int,(sys.stdin.readline().rstrip().split())))
Sum = 0
for j in range(N):
    Sum += P[j] * (len(P)-j)

print(Sum)
