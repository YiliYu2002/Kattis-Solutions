def main():
    num = int(input())
    for i in range(num):
        line_1 = input()
        line_2 = input()
        line_3 = input()
        x = 0
        o = 0
        for j in range(3):
            if line_1[j] == 'X':
                x += 1
            elif line_1[j] == 'O':
                o += 1

            if line_2[j] == 'X':
                x += 1
            elif line_2[j] == 'O':
                o += 1

            if line_3[j] == 'X':
                x += 1
            elif line_3[j] == 'O':
                o += 1

        if x - 1 == o or x == o:
            print('yes')
        elif x >= 3 and o >= 3:
            print('no')
        else:
            print('no')

        if i != num - 1:
            empty = input()

main()