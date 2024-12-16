N = int(input())

for i in range(N//5,  -1 , -1):
    re = N - 5 * i
    if re % 3 == 0:
        j = re // 3
        print(i+j)
        break
else:
    print(-1)
