# memo = {}
#
#
# def digit_sum(n):
#     ans = 0
#     while n > 0:
#         ans += n % 10
#         n //= 10
#     return ans
#
#
# def count(n):
#     if n <= 0:
#         return 0
#     if n in memo:
#         return memo[n]
#     if n % 10 == 0:
#         ans = 10 * count(n // 10) + 45 * (n // 10)
#         memo[n] = ans
#         return ans
#     ans = count(n - 1) + digit_sum(n - 1)
#     memo[n] = ans
#     return ans
#
#
# n = int(input())
# for _ in range(n):
#     a, b = map(int, input().split())
#     print(count(b + 1) - count(a))
#     print(memo)


def DFS(pos, pre, up, limit, word):
    global dp

    if pos == len(word):
        return 1

    now = dp[pos][pre][up]
    if not limit and now != -1:
        return now

    sol = 0
    d = int(word[pos]) if limit else 9

    for i in range(d + 1):
        if up:
            if i >= pre:
                sol += DFS(pos + 1, i, up, limit and (i == d), word)
            else:
                sol += DFS(pos + 1, i, 0, limit and (i == d), word)
        elif i <= pre:
            sol += DFS(pos + 1, i, 0, limit and (i == d), word)

    if not limit:
        dp[pos][pre][up] = sol

    return sol


word = input()
flag = -1
for i in range(1, len(word)):
    if word[i] < word[i - 1]:
        flag = 0
    if flag == 0 and word[i] > word[i - 1]:
        flag = 1
        break

if flag == 1:
    print("-1")
else:
    global dp
    dp = [[[-1 for _ in range(2)] for _ in range(10)] for _ in range(len(word))]
    print(DFS(0, 0, 1, 1, word) - 1)

'''
身为一个爱吃+爱锐评的人，打算出一系列“里士满美食地图”，探店里士满美食
希望可以拯救在里士满，aka最美(也不一定)城乡结合部，为下顿吃什么发愁的朋友

Melting Pot，餐厅定位：高档创新融合餐厅
味道:不喜欢芝士的人绕道
特色:瑞士芝士火锅/巧克力火锅，法式炖菜(火锅形式)等等
环境:这个餐厅氛围很好，有足够的私密空间，比较适合约会
人均: 约70刀

点菜: Big Night Out Dinners ($114)
1. Classic Alpine Cheese Fondue
2. Melting Pot House + California
3. Cooking Style: Coq Au Vin
4. Flaming Turtle Chocolate Fondue
第一轮:餐前面包沾芝士火锅(加果蔬)
第二轮:很普通的沙拉
第三轮:主菜，选的锅底是法式红酒炖鸡(Coq Au Vin)的汤，类似中式菌菇，没太多味道；食材比较丰富但量比较少，最喜欢里面的虾和照烧风味牛肉
第四轮:甜品，我们吃的比较着急，最后打包带走了。不太好评价，如果堂食应该会比较不错

总结一下，如果是来享受美式慰藉的，Melting Pot之外还有很多更好更便宜的选择。如果是来庆祝生日，来约会，或者单纯想体验一把创意菜，Melting Pot绝对可以满足要求。
'''
