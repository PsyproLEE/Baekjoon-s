N = int(input())
A = list(map(int,input().split()))


A = list(map(lambda x : x/max(A)*100,A))
result = sum(A)/N

print(result)