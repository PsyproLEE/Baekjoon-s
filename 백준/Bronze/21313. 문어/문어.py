n= int(input())
if n % 2 ==0 :
    ans = [1,2] * (n//2)
else:
    ans = [1,2] * (n//2) + [3]
print(*ans)