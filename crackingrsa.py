case = int(input())
p, q = 0, 0


def gcdExtended(a, b):
    # Base Case
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcdExtended(b % a, a)
    # Update x and y using results of recursive
    # call
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def solve(a, b):
    g, x, _ = gcdExtended(a, b)
    if g != 1:
        return -1
    else:
        return x % b


for _ in range(case):
    n, e = map(int, input().split())
    for i in range(2, n):
        if n % i == 0:
            p = n / i
            q = i
            break
    res = (p - 1) * (q - 1)
    sol = 1

    print(int(solve(e, res)))

    # print(solve(e, res))

    # while True:
    #     tem = (e * sol - 1) % res
    #     if tem == 0:
    #         print(sol)
    #         break
    #     else:
    #         sol += 1
