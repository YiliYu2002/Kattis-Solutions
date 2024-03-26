from sys import stdin
from collections import deque


m, n = map(int, stdin.readline().split())
start = (-1, -1)
grid = [[] for _ in range(n)]
for i in range(n):
    grid[i] = list(map(str, stdin.readline().rstrip()))
    if 'P' in grid[i]:
        start = i, grid[i].index('P')

vis = set()
q = deque([start])
sol = 0
while q:
    curr = q.popleft()
    flag = True
    if curr in vis:
        continue
    vis.add(curr)
    x, y = curr
    if grid[x][y] == 'G':
        sol += 1
    loc = [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]
    for i in loc:
        xx, yy = i
        if grid[xx][yy] == 'T':
            flag = False
            break
    if flag:
        for i in loc:
            xx, yy = i
            if grid[xx][yy] != '#':
                q.append((xx, yy))
print(sol)




