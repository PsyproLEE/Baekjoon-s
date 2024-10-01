a = int(input())
list = [[0] for _ in range(a) ]

for i in range(a):

    R ,S = input().split() 
    list[i] = "".join([char * int(R) for char in S]) 

for j in range(a):
    print(list[j])