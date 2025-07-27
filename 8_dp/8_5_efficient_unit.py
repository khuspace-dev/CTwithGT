N, M = map(int, input().split())
units = []
dp = [10001] * (M + 1)

for _ in range(N):
    units.append(int(input()))

dp[0] = 0
for unit in units:
    if unit > M:
        continue
    for i in range(1, M + 1):
        if i - unit != 10001:
            dp[i] = min(dp[i - unit] + 1, dp[i])

if dp[M] == 10001:
    print(-1)
else:
    print(dp[M])
