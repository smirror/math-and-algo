from math import sqrt

n = int(input())
ans = set()

for i in range(1, int(sqrt(n))+1000):
    if n % i == 0:
        ans.add(i)
        ans.add(n // i)

print(*ans, sep='\n')