n = int(input())
a = list(map(int, input().split()))

# dp[i][j][k] : 最初の i 枚のカードから j 枚選んで合計 k を作る方法の数
dp = [[[0] * 1001 for _ in range(6)] for _ in range(n + 1)]
dp[0][0][0] = 1  # 0 枚選んで合計 0 を作る方法は 1 通り

for i in range(1, n + 1):
    for j in range(6):  # j は選ぶカードの枚数、最大5枚
        for k in range(1001):  # k は合計、最大1000
            dp[i][j][k] = dp[i-1][j][k]
            if j > 0 and k >= a[i-1]:
                dp[i][j][k] += dp[i-1][j-1][k-a[i-1]]

print(dp[n][5][1000])
