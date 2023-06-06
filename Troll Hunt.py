def main():
    num = input().split()
    stone = int(num[0])
    kni = int(num[1])
    group = int(num[2])
    res = (stone - 1) // (kni // group)
    if res * (kni // group) < stone - 1:
        res += 1
    return res


print(main())
