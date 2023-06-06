def main():
    line = input().split()
    r1 = int(line[0])
    s = int(line[1])
    r2 = r1 + (s - r1) * 2
    return r2


print(main())
