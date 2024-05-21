from math import sqrt, ceil, gcd

n = int(input())
ans = list()


for i in range(2, ceil(sqrt(n)) + 1):
    while n % i == 0:
        ans.append(gcd(n, i))
        n //= i

if n > 1:
    ans.append(n)

print(*ans)
