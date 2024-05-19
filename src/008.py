n, s = map(int, input().split())
ans = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if s >= i + j:
            ans += 1
print(ans)
