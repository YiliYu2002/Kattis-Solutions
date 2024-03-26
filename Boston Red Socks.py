import math


def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


while True:
    flag = False
    p, q = map(int, input().split())
    if p + q == 0:
        break
    gd = gcd(p, q)
    # edge case
    if p == 0:
        print("0 2")
        continue
    if p == q:
        print("2 0")
        continue

    p //= gd
    q //= gd

    for i in range(3, 50001):
        tem = i * (i - 1) * p
        if tem % q != 0:
            continue
        tem //= q
        mid, l, r = 0, 1, i

        while l < r:
            mid = (l + r) // 2
            M = mid * (mid - 1)
            if M < tem:
                l = mid + 1
            elif M > tem:
                r = mid
            else:
                flag = True
                break

        if flag:
            print(mid, i - mid)
        else:
            print("impossible")

        # if i * (i - 1) % q != 0:
        #     continue
        # j = i * (i - 1) // q * p
        # tmp = int(math.sqrt(j + 0.5))
        # if tmp * (tmp + 1) != j:
        #     continue
        # if tmp >= 1:
        #     break

    # if i == 50001:
    #     print("impossible")
    # else:
    #     print(tmp + 1, i - tmp - 1)
    #
    #     for total in range(3, 50001):
    #         N = total * (total - 1) * P
    #         if N % Q != 0:
    #             continue
    #         N //= Q
    #         l, r = 1, total
    #
    #         while l < r:
    #             m = (l + r) // 2
    #             M = m * (m - 1)
    #             if M < N:
    #                 l = m + 1
    #             elif M > N:
    #                 r = m
    #             else:
    #                 flag = True
    #                 break

