import sys

for line in sys.stdin:
    A, B = map(int, line.split())
    if A == B == 0:
        break
    print(A + B)