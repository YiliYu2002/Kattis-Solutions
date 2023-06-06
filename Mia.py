dic = {'12': 100, '21': 100, '66': 99, '55': 98, '44': 97, '33': 96, '22': 95, '11': 94}
flag = True
line = input().split()
if line == ['0', '0', '0', '0']:
    flag = False

while flag:
    p1 = line[0] + line[1]
    p2 = line[2] + line[3]
    if p1 in dic:
        p1 = dic[p1]
    else:
        p1 = max(int(line[0]), int(line[1])) * 10 + min(int(line[0]), int(line[1]))

    if p2 in dic:
        p2 = dic[p2]
    else:
        p2 = max(int(line[2]), int(line[3])) * 10 + min(int(line[2]), int(line[3]))

    if p1 == p2:
        print('Tie.')
    elif p1 > p2:
        print('Player 1 wins.')
    else:
        print('Player 2 wins.')

    line = input().split()
    if line == ['0', '0', '0', '0']:
        flag = False
