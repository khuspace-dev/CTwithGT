T = int(input())

for _ in range(T):
    mine = []

    n, m = map(int, input().split())
    lines = list(map(int, input().split()))
    for i in range(n):
        mine.append(lines[i * m : i * m + m])

    dp = []
    for _ in range(n):
        dp.append([-1 for _ in range(m)])

    # init
    for i in range(n):
        dp[i][0] = mine[i][0]
    for col in range(1, m):
        for row in range(n):
            if row > 0 and row < n - 1:
                dp[row][col] = (
                    max(dp[row - 1][col - 1], dp[row][col - 1], dp[row + 1][col - 1])
                    + mine[row][col]
                )
            elif row > 0:
                dp[row][col] = (
                    max(dp[row - 1][col - 1], dp[row][col - 1]) + mine[row][col]
                )
            else:
                dp[row][col] = (
                    max(dp[row][col - 1], dp[row + 1][col - 1]) + mine[row][col]
                )

    maximum = 0
    for row in range(n):
        maximum = max(maximum, dp[row][m - 1])
    print(maximum)
