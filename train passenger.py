def main():
    line = input().split()
    n = int(line[1])
    C = int(line[0])
    res = 0
    flag = True
    for i in range(n):
        line = input().split()
        left = int(line[0])
        went = int(line[1])
        wait = int(line[2])
        if res - left < 0:
            flag = False
        res = res + went - left
        if res > C or (res < C and wait > 0):
            flag = False
    if res != 0:
        flag = False
    if flag:
        print('possible')
    else:
        print('impossible')


main()
