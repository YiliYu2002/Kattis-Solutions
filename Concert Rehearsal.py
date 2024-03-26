import bisect

N, P, K = map(int, input().split())
pre_calc, rem = [0] * N, [(0, 0)] * N
pre_calc[0] = int(input())
for i in range(1, N):
    pre_calc[i] = pre_calc[i - 1] + int(input())
# rem[0] = (bisect.bisect_left(pre_calc, P % pre_calc[-1]), P // pre_calc[-1])
# for i in range(1, N):
#     ind = bisect.bisect_left(pre_calc, (P + pre_calc[i - 1]) % pre_calc[-1])
#     rem[i] = (ind, (P + pre_calc[i - 1]) // pre_calc[-1])
# {0:0}
flag = True
dic_1 = {0: 0}
dic_2 = {0: 0}
p = 0
# while flag:
#     if p == 0:
#
#     dic_1[]

# for i in range(1, 100):
#     p, _ = rem[dic[i - 1]]
#     dic[i] = p
# print(dic)
# print(pre_calc)
print(rem)
