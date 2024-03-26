while True:
    cases = int(input())
    if cases == 0:
        exit()
    else:
        am = {}
        pm = {}
        for _ in range(cases):
            a, b = input().split()
            h, m = map(int, a.split(':'))
            if h == 12:
                h = 0
            k = h * 60 + m
            if b == 'a.m.':
                v = a + ' ' + b
                if k in am.keys():
                    am[k].append(v)
                else:
                    am[k] = [v]
            else:
                v = a + ' ' + b
                if k in pm.keys():
                    pm[k].append(v)
                else:
                    pm[k] = [v]

    for i in sorted(am.keys()):
        for j in am[i]:
            print(j)

    for i in sorted(pm.keys()):
        for j in pm[i]:
            print(j)
    print('\n')
