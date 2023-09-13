from sys import stdin
for line in stdin:
    n = int(line)
    if n == 0:
        break

    if n == 1:
        print(1)
    else:
        res = (n - 1) * 2
        print(res)
