def main():
    num_people = int(input())
    position_list = input().split()
    lis = process(num_people, position_list)
    print(*lis, sep=' ')


def process(p, lis):
    pos = [1] * p
    count = 2
    for i in range(len(lis)):
        pos[int(lis[i]) + 1] = count
        count += 1
    return pos


main()
