from sys import stdin
flag = False
dic = {}
# fee = {}
day = 1
for line in stdin:
    t = line.split()
    if t[0] == 'OPEN':
        fee = {}
        if flag:
            print('\n')
        print('Day', day)
        flag = True

    elif t[0] == 'CLOSE':
        for i in sorted(fee.keys()):
            print(i, '$' + "{:.2f}".format(fee[i]))
        day += 1
    else:
        action, ppl, num = t[0], t[1], int(t[2])
        if action == 'ENTER':
            dic[ppl] = num
            if ppl not in fee:
                fee[ppl] = 0
        else:
            fee[ppl] += 0.10 * (num - dic[ppl])



