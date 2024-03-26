# import heapq
# import math
#
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]
#
# n, m = map(int, input().split())
#
#
# def check_bound(x, y):
#     return 0 <= x < n and 0 <= y < m
#
#
# val = [[0] * m for _ in range(n)]
# best = [[math.math.inf] * m for _ in range(n)]
# vis = [[False] * m for _ in range(n)]
# for i in range(n):
#     val[i] = list(map(int, input().split()))
# best[0][0] = 0
# q = [(0, 0, 0)]
# heapq.heapify(q)
#
# while q:
#     currval, currx, curry = heapq.heappop(q)
#     if vis[currx][curry]:
#         continue
#     vis[currx][curry] = True
#     for i in range(4):
#         nextx, nexty = currx + dx[i], curry + dy[i]
#         if not check_bound(nextx, nexty):
#             continue
#         nextval = max(0, val[nextx][nexty] - val[currx][curry], best[currx][curry])
#         if best[nextx][nexty] > nextval:
#             best[nextx][nexty] = nextval
#             heapq.heappush(q, (nextval, nextx, nexty))
#
# print(best[n - 1][m - 1])
#


import heapq
import math

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def main():
    n, m = map(int, input().split())
    v = [[-1] * (m + 2) for _ in range(n)]

    for i in range(n):
        v[i][1:m + 1] = map(int, input().split())

    best = [[math.inf] * (m + 2) for _ in range(n)]
    vis = [[False] * (m + 2) for _ in range(n)]
    best[0][0] = 0
    q = [(0, 0, 0)]

    while q:
        currval, currx, curry = heapq.heappop(q)
        if vis[currx][curry]:
            continue
        vis[currx][curry] = True

        for i in range(4):
            nextx, nexty = currx + dx[i], curry + dy[i]
            if 0 <= nextx < n and 0 <= nexty < m + 2:
                nextval = max(best[currx][curry], v[nextx][nexty])
                if nextval < best[nextx][nexty]:
                    best[nextx][nexty] = nextval
                    heapq.heappush(q, (nextval, nextx, nexty))

    print(best[0][m + 1])


if __name__ == "__main__":
    main()
