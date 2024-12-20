import sys

N,M = map(int,sys.stdin.readline().rstrip().split())
N_set = set()
M_set = set()
for i in range(N):
    N_set.add(sys.stdin.readline().rstrip())
for i in range(M):
    M_set.add(sys.stdin.readline().rstrip())

result = sorted(N_set & M_set)
print(len(result))
for r in result:
    print(r)