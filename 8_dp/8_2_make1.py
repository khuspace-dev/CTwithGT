X = int(input())

INF = 30001
dp = [INF] * 30001


def make1(x):
    # base case
    if x == 1:
        return 0

    # dp case
    if dp[x] != INF:
        return dp[x]

    # general case
    if x % 5 == 0:
        dp[x] = min(dp[x], make1(x // 5) + 1)
    elif x % 3 == 0:
        dp[x] = min(dp[x], make1(x // 3) + 1)
    elif x % 2 == 0:
        dp[x] = min(dp[x], make1(x // 2) + 1)

    dp[x] = min(dp[x], make1(x - 1) + 1)
    return dp[x]


print(make1(26))
