result = []

while True:    
    sides = list(map(int,input().split()))

    if sum(sides) == 0:
        break

    sides.sort()
    if sides[2]**2 == sides[1]**2 +sides[0]**2:
        result.append("right")
    else:
        result.append("wrong")

for r in result:
    print(r)