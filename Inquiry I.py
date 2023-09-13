case = int(input())
prod = [0]
lis = []
for _ in range(case):
    num = int(input())
    prod.append(prod[-1] + num * num)
    lis.append(num)

lis.append(0)
for i in range(case - 1, -1, -1):
    lis[i] += lis[i+1]

sol = 0
for i in range(case):
    sol = max(sol, lis[i] * prod[i])

print(sol)