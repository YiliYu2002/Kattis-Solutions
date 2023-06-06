def main():
    num = int(input())
    lis = []
    for i in range(num):
        n = int(input())
        lis.append(n)
    for i in range(1001):
        if isPossible(lis, 1000 + i):
            return 1000 + i
        elif isPossible(lis, 1000 - i):
            return 1000 - i


def isPossible(elements, target):
    dp = [False] * (target + 1)
    dp[0] = True
    for ele in elements:
        for j in range(target, ele - 1, -1):
            if dp[j - ele]:
                dp[j] = True
    return dp[target]


print(main())
