result = []
while True:

    A = input()
    if A == '0':
        break
    
    B = len(A)
    is_palindrome = True
    
    
    for i in range(B//2):
        if A[i] != A[-i-1]:
            is_palindrome = False
            break
    if is_palindrome:
        result.append("yes")

    else: 
        result.append("no")

   


for res in result:
    print(res)