flag = True
wrong = {}
time = {}
lis = []
line = input()
if line == '-1':
    flag = False
while flag:
    line = line.split()
    if line[2] == 'right' and line[2] not in time:
        time[line[1]] = line[0]
        lis.append(line[1])
    else:
        if line[1] in wrong:
            wrong[line[1]] += 1
        else:
            wrong[line[1]] = 1

    line = input()
    if line == '-1':
        flag = False
res = 0
for k in lis:
    if k in wrong:
        res += 20 * int(wrong[k])
    res += int(time[k])
print(len(lis), ' ', res)
