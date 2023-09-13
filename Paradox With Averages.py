case = int(input())
for i in range(case):
    bl = input()
    nc, ne = map(int, input().split())
    lc = list(map(int, input().split()))
    le = list(map(int, input().split()))
    ac = sum(lc) / nc
    ae = sum(le) / ne
    ans = 0
    for j in lc:
        if ac > j > ae:
            ans += 1
    print(ans)
