# import math
#
#
# def DP(n, n1, n5, n10, vis, dp):
#     if vis[n1][n5][n10]:
#         return dp[n1][n5][n10]
#     elif n == 0:
#         vis[n1][n5][n10] = 1
#         dp[n1][n5][n10] = 0
#         return dp[n1][n5][n10]
#     else:
#         dp[n1][n5][n10] = math.inf
#         if n1 >= 8:
#             dp[n1][n5][n10] = min(dp[n1][n5][n10], DP(n - 1, n1 - 8, n5, n10, vis, dp) + 8)
#         if n5 >= 1 and n1 >= 3:
#             dp[n1][n5][n10] = min(dp[n1][n5][n10], DP(n - 1, n1 - 3, n5 - 1, n10, vis, dp) + 4)
#         if n5 >= 2:
#             dp[n1][n5][n10] = min(dp[n1][n5][n10], DP(n - 1, n1 + 2, n5 - 2, n10, vis, dp) + 2)
#         if n10 >= 1:
#             dp[n1][n5][n10] = min(dp[n1][n5][n10], DP(n - 1, n1 + 2, n5, n10 - 1, vis, dp) + 1)
#         if n10 >= 1 and n1 >= 3:
#             dp[n1][n5][n10] = min(dp[n1][n5][n10], DP(n - 1, n1 - 3, n5 + 1, n10 - 1, vis, dp) + 4)
#         vis[n1][n5][n10] = 1
#         return dp[n1][n5][n10]
#
#
# for _ in range(int(input())):
#     num, N1, N5, N10 = map(int, input().split())
#     vis = [[[0] * 100 for _ in range(200)] for _ in range(700)]
#     dp = [[[0] * 100 for _ in range(200)] for _ in range(700)]
#     print(DP(num, N1, N5, N10, vis, dp))
#
#


for _ in range(int(input())):
    c, n_1, n_5, n_10 = map(int, input().split())
    extras = n_10 * 10 + n_5 * 5 + n_1 - 8 * c
    S = [[[0] * (n_10 + 1) for _ in range(n_5 + n_10 + 2)] for _ in range(c + 1)]
    for i in range(1, c + 1):
        for j in range(n_5 + n_10 + 1):
            for k in range(n_10 + 1):
                ans = S[i - 1][j][k] + 8
                if k >= 1:
                    ans = min(ans, S[i - 1][j][k - 1] + 1)
                    if extras + (c * 8 - k * 10 - j * 5) >= 3:
                        ans = min(ans, S[i - 1][j + 1][k - 1] + 4)
                if j >= 1:
                    ans = min(ans, S[i - 1][j - 1][k] + 4)
                if j >= 2:
                    ans = min(ans, S[i - 1][j - 2][k] + 2)
                S[i][j][k] = ans
    print(S[c][n_5][n_10])
