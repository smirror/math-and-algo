from collections import Counter

n = int(input())
a = list(map(int, input().split()))
A = Counter(a)
ans = 0
for i in set(a):
    tmp = 100000 - i
    if i == tmp:
        ans += A[i] * (A[i] - 1) // 2
    elif A[tmp]:
        ans += A[tmp] * A[i]
    A.pop(i, None)
    A.pop(tmp, None)
print(ans)
