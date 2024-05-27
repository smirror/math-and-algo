from collections import Counter

n = int(input())
a = list(map(int, input().split()))

cnt = Counter(a)
ans = 0
for i, v in cnt.items():
    ans += v * (v - 1) // 2
print(ans)
