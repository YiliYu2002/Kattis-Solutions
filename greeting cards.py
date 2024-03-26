# 2018^2 = x^2 + y^2

n = int(input())
ans = 0
s = set()
dx = [2018, -2018, 0, 0, 1118, 1118, -1680, 1680, 1680, -1680, -1118, -1118]
dy = [0, 0, 2018, -2018, -1680, 1680, 1118, 1118, -1118, -1118, 1680, -1680]

for i in range(n):
    x, y = map(int, input().split())
    for j in range(12):
        n_x = x + dx[j]
        n_y = y + dy[j]
        if (n_x, n_y) in s:
            ans += 1
    s.add((x, y))

print(ans)
