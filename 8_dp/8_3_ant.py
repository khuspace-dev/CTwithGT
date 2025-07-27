N = int(input())
storages = list(map(int, input().split()))
dp = [-1] * N

dp[0] = storages[0]
dp[1] = max(dp[0], storages[1])
for i in range(2, N):
    dp[i] = max(dp[i - 2] + storages[i], dp[i - 1])

print(dp[N - 1])
