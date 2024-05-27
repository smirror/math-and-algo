from math import lcm

n, x, y = map(int, input().split())
print(n // x + n // y - n // lcm(x, y))
