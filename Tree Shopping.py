# n, k = map(int, input().split())
# trees = list(map(int, input().split()))
#
# dic = {}
# for i in range(k):
#     if trees[i] not in dic:
#         dic[trees[i]] = 1
#     else:
#         dic[trees[i]] += 1
#
# sol = max(dic.keys()) - min(dic.keys())
#
# for i in range(1, n - k + 1):
#     if dic[trees[i - 1]] == 1:
#         del dic[trees[i - 1]]
#     else:
#         dic[trees[i - 1]] -= 1
#     if trees[i + k - 1] not in dic:
#         dic[trees[i + k - 1]] = 1
#     else:
#         dic[trees[i + k - 1]] += 1
#     tem = max(dic.keys()) - min(dic.keys())
#     sol = min(sol, tem)
#     # print(dic)
#     # print(sol)
#
# print(sol)

