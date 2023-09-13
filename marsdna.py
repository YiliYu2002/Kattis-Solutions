n, k, r = map(int, input().split())
dna = list(map(int, input().split()))
counts = [0] * k

for i in range(n):
    counts[dna[i]] += 1

dic = {}
num = 0

for _ in range(r):
    b, q = map(int, input().split())
    if q > counts[b]:
        print("impossible")
        exit(0)
    dic[b] = q
    num += 1

sol = float('inf')
cur = {}
i, j = 0, 0

while True:
    if num > 0:
        if j == n:
            break
        cur[dna[j]] = cur.get(dna[j], 0) + 1
        if cur[dna[j]] == dic.get(dna[j], 0):
            num -= 1
        j += 1
    else:
        sol = min(sol, j - i)
        if cur.get(dna[i], 0) == dic.get(dna[i], 0):
            num += 1
        cur[dna[i]] -= 1
        i += 1

print(sol)
