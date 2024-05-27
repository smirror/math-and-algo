n, s = map(int, input().split())
a = list(map(int, input().split()))

dp = [[0] * (s + 1) for _ in range(n + 1)]
dp[0][0] = 1
for i in range(1, n + 1):
    for j in range(s + 1):
        dp[i][j] = dp[i-1][j]
        if j >= a[i-1]:
            dp[i][j] += dp[i-1][j - a[i-1]]

if dp[-1][-1] > 0:
    print("Yes")
else:
    print("No")
