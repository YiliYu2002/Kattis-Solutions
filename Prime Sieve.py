from sys import stdin

n, q = map(int, input().split())
prime = [True] * (n + 1)
prime[0] = False
prime[1] = False
p = 2
count = 0
while p * p <= n:
    if prime[p]:
        for i in range(p * p, n + 1, p):
            prime[i] = False
    p += 1
print(sum(prime))
for line in stdin:
    nbr = int(line)
    if prime[nbr]:
        print(1)
    else:
        print(0)
