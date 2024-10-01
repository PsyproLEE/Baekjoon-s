N = int(input())

for i in range(N // 5, -1, -1):
    reminder = N - 5 * i
    if reminder % 3 == 0:
        j = reminder // 3
        print(i + j)
        break
else:
    print(-1)