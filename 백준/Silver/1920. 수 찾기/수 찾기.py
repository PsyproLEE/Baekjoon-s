import sys


def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return 0



N = int(sys.stdin.readline().strip())
line = list(map(int,sys.stdin.readline().strip().split()))
line.sort()

M = int(sys.stdin.readline().strip())
Answer = list(map(int,sys.stdin.readline().strip().split()))

for i in range(M):
    print(binary_search(line,Answer[i]))