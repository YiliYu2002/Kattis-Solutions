import math


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


def get_factors(n):
    factors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
            factors.append(n // i)

    if math.isqrt(n) ** 2 == n:  # n is a perfect square
        factors.pop()

    return factors


case = int(input())
lis = []
cd = []
gcd = 0
for _ in range(case):
    lis.append(int(input()))
lis.sort()

for i in range(len(lis)):
    for j in range(i + 1, len(lis)):
        gcd = gcdExtended(gcd, lis[j] - lis[i])[0]

for k in get_factors(gcd):
    if k != 1:
        print(k, end=' ')
