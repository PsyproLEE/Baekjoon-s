N = int(input())
store = []

for _ in range(N):
    store.append(input())

store = list(set(store))  

store.sort(key=lambda x: (len(x), x)) ## key라는 매개변수 활용방법!

for s in store:
    print(s)