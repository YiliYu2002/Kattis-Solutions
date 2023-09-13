from sys import stdin

for line in stdin:
    t = line.split()
    l, n = int(t[0]), int(t[1])
    sol = 1
    rem = l % n
    while rem != 0:
        sol += 1
        n -= rem
        rem = l % n
        # print(n, rem)
    print(sol)
