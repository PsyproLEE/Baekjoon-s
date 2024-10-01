x, y = map(int,(input().split()))

x_prime_factor = []
y_prime_factor = []

i = 2
while x > 1:
    if x % i == 0:
        x_prime_factor.append(i)
        x //= i
    else:
        i += 1

i = 2
while y > 1:    
    if y % i == 0:
        y_prime_factor.append(i)
        y //= i
    else:
        i += 1

gcd_value = 1
common_factors = set(x_prime_factor) & set(y_prime_factor)
for factor in common_factors:
    gcd_value *= factor ** min(x_prime_factor.count(factor), y_prime_factor.count(factor))

lcm_value = 1
all_factors = set(x_prime_factor) | set(y_prime_factor)
for factor in all_factors:
    lcm_value *= factor ** max(x_prime_factor.count(factor), y_prime_factor.count(factor))
        

print(gcd_value)
print(lcm_value)