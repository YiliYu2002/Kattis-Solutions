def sum_sol(sol, index):
    total = 0
    i = index
    while i > 0:
        total += sol[i - 1]
        i &= i - 1
    return total


def update_sol(sol, index, value):
    i = index
    while i < len(sol):
        sol[i] += value
        i |= i + 1


def get_val(sol, index):
    return sum_sol(sol, index + 1) - sum_sol(sol, index)


n, k = map(int, input().split())
sol = [0] * (n + 1)

for _ in range(k):
    c = input().split()

    if c[0] == 'F':
        x = int(c[1])
        val = get_val(sol, x)

        if val == 0:
            val = 1
        else:
            val = -1
        update_sol(sol, x, val)
        val = get_val(sol, x)

    elif c[0] == 'C':
        x, y = int(c[1]), int(c[2])
        print(sum_sol(sol, y + 1) - sum_sol(sol, x))
