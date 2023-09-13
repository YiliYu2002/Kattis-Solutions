import math

n, k = map(int, input().split())
lis = []
tem = []
for _ in range(n):
    lis.append(int(input()))
lis.sort()
# tem.append(lis[0] + 1000)
#
# for j in range(1, n):
#     p = 0
#     while p < len(tem) and tem[p] <= lis[j]:
#         p += 1
#     if p == len(tem):
#         tem.append(lis[j] + 1000)
#     else:
#         tem[p] = lis[j] + 1000
#     print(tem)
# print(lis)
# print(len(tem) // k) if len(tem) % k == 0 else print(len(tem) // k + 1)
max_count = 0
count = 1
now = 0

for i in range(1, n):
    while lis[i] - lis[now] >= 1000:
        count -= 1
        now += 1
    count += 1
    max_count = max(max_count, count)

print(math.ceil(max_count / k)) if n != 1 else print('1')
