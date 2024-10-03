N, K = map(int,(input().split()))

def fatctorial(m):
    fact = 1
    for i in range(1,m+1):
        fact *= i
    return fact

print(int(fatctorial(N)/(fatctorial(K)*fatctorial(N-K)))) 