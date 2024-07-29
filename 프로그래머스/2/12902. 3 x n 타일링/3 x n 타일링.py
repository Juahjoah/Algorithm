def solution(n):
    if n % 2 != 0:
        return 0

    mod = 1000000007
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[2] = 3

    for i in range(4, n + 1, 2):
        dp[i] = dp[i - 2] * 3
        for j in range(4, i + 1, 2):
            dp[i] += dp[i - j] * 2
        dp[i] %= mod

    return dp[n]