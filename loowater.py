while True:
    h, k = map(int, input().split())
    if k == 0 and h == 0:
        break

    heads = []
    knights = []
    for _ in range(h):
        heads.append(int(input()))
    for _ in range(k):
        knights.append(int(input()))

    total = 0
    knights.sort()
    heads.sort()

    while knights and heads:
        if knights[0] >= heads[0]:
            heads.pop(0)
            total += knights[0]
        knights.pop(0)

    if heads:
        print("Loowater is doomed!")
    else:
        print(total)
