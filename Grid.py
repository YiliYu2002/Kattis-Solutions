def main():
    mn = input().split(' ')
    N = int(mn[0])
    M = int(mn[1])
    G = [] * N
    for i in range(N):
        line = input().split()
        for j in range(M):
            G[i].append(int(line[0][j]))
    dp = [[-1] * N for _ in range(M)]
    dp[0][0] = 0
    print(G)
    print(dp)


main()