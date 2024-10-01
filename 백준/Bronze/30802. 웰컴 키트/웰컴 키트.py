import math

N = int(input()) #참가자수
Cloth_size = list(map(int,(input().split()))) #각 사이즈 별 옷 개수
T, P = map(int,(input().split())) #티셔츠 묶음, 펜 묶음 수

Count_cloth = 0
for i in Cloth_size:
    Count_cloth += math.ceil(i/T)
Bundle = N//P 
Remainder = N%P

print(Count_cloth) 
print(Bundle, Remainder)
