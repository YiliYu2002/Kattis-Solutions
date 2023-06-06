def isPrime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def solve(n):
    res = 0
    i = 2
    while n > 1:
        if n % i == 0:
            res += i
            n /= i
            if isPrime(n):
                res += n
                break
            else:
                i += 1
    return res


def main():
    flag = True
    while flag:
        res = 0
        line = input()
        if line == '4':
            break
        while not isPrime(int(line)):
            line = solve(int(line))
            res += 1
        print(line, ' ', res)


main()