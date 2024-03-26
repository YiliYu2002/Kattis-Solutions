# case = int(input())
# for _ in range(case):
#     # input
#     num_color = int(input())
#     mat = [[True] * num_color for _ in range(num_color)]
#     # DFS like visited or not
#     color_use = [False] * num_color
#
#     # dic {color: index}
#     dic = {}
#     c = input().split()
#     print(c)
#     for i in range(num_color):
#         dic[c[i]] = i
#     num_restrict = int(input())
#     # DP initialization
#     for _ in range(num_restrict):
#         c1, c2 = map(str, input().split())
#         mat[dic[c1]][dic[c2]], mat[dic[c2]][dic[c1]] = False, False
#
#     ans = 0
#     sol = []
#     ans_string = ""
#
#
#     def backtrack(prev):
#         if False not in color_use:
#             global ans
#             ans += 1
#             if ans == 1:
#                 global ans_string
#                 ans_string = ' '.join(sol)
#         for j in dic.keys():
#             if not color_use[dic[j]]:
#                 continue
#             if prev == '' or not mat[dic[prev][j]] or not mat[dic[j][prev]]:
#                 continue
#             color_use[dic[j]] = False
#             sol.append(j)
#             backtrack(j)
#             color_use[dic[j]] = True
#             sol.pop()
#
#     backtrack('')
#     print(ans)
#     print(ans_string)

"""
num_tc = int(input())
for _ in range(num_tc):
    n = int(input())
    colors = list(input().split())
    colour_mask = {c: 1 for c in colors}

    num_hideous = int(input())
    bad = {}
    for i in range(num_hideous):
        a, b = input().split()
        if a in bad:
            bad[a].add(b)
        else:
            bad[a] = {b}

        if b in bad:
            bad[b].add(a)
        else:
            bad[b] = {a}

    ans = 0
    sol = []
    ans_string = ""

    def backtrack(prev):
        if sum(colour_mask.values()) == 0:
            global ans
            ans += 1
            if ans == 1:
                global ans_string
                ans_string = ' '.join(sol)
        for i in colors:
            if colour_mask[i] == 0:
                continue
            if (prev in bad) and (i in bad[prev]):
                continue
            colour_mask[i] = 0
            sol.append(i)
            backtrack(i)
            colour_mask[i] = 1
            sol.pop()

    backtrack('')
    print(ans)
    print(ans_string)
"""


def recurse():
    global ways, best, used, good
    global here
    here = []
    if len(here) == n:
        if not best:
            best = here[:]
        ways += 1
        return
    for i in range(n):
        if not used[i]:
            if here and not good[here[-1]][i]:
                continue
            used[i] = True
            here.append(i)
            recurse()
            here.pop()
            used[i] = False


def solve():
    global n, ways, best, used, here, good
    n = int(input())
    used = [False] * n

    color = {}
    colors = []
    s = input().split()
    for i in range(n):
        color[s[i]] = i
        colors.append(s[i])
    print(colors)

    good = [[True] * n for _ in range(n)]
    t = int(input())
    for _ in range(t):
        s1, s2 = map(str, input().split())
        n1 = color[s1]
        n2 = color[s2]
        good[n1][n2] = False
        good[n2][n1] = False

    recurse()

    print(ways)
    for i in best:
        print(colors[i], end=" ")
    print()

    ways = 0
    best = []


if __name__ == "__main__":
    cases = int(input())
    for _ in range(cases):
        solve()
