import sys

N = int(sys.stdin.readline())
save = []
for i in range(N):
    save.append(int(sys.stdin.readline()))

save.sort()

for i in range(N):
    print(save[i])