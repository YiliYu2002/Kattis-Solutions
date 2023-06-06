def main():
    num = int(input())
    lis = input().split()
    dic = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for i in range(len(lis)):
        dic[int(lis[i])] += 1

    for j in range(6, 0, -1):
        if dic[j] == 1:
            res = str(lis.index(str(j)) + 1)
            return res
    res = "none"
    return res


print(main())
