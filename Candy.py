case = int(input())

for i in range(case):
    b = input()
    n = int(input())
    res = 0
    for j in range(n):
        res += int(input())
    print('YES') if res % n == 0 else print('NO')
# while i <= case:
#     tem = input()
#     if len(tem) != 0:
#         res += int(tem)
#         num += 1
#     else:
#         if num != 0:
#             print('YES') if res % num == 0 else print('NO')
#             res, num = 0, 0
#         i += 1
#     print((num, res))
#
# print('YES') if res % num == 0 else print('NO')

# from sys import stdin
# res = 0
# num = 0
# case = int(input())
#
# for line in stdin:
#     # print(len(line))
#     if len(line) != 1:
#         res += int(line)
#         num += 1
#     else:
#         if num != 0:
#             print('YES') if res % num == 0 else print('NO')
#             res, num = 0, 0
# print('YES') if res % num == 0 else print('NO')
