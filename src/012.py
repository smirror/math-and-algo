from math import sqrt

n = int(input())

for i in range(2, int(sqrt(n))):
    if n % i == 0:
        print("No")
        exit()

print("Yes")
