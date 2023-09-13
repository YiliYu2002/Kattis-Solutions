lis = [1] * 21
nums = int(input())
power = 0
sol = 0

for i in range(1, 21):
    lis[i] = 2 * lis[i - 1]

for i in range(21):
    if lis[i] >= nums:
        sol = lis[i]
        power = i
        break

if lis[power] == nums:
    print(sol, 0)
elif nums % 2 == 1:
    print(sol, power)
else:
    nums -= sol // 2
    num_break = power
    while num_break >= 0:
        if nums >= lis[num_break]:
            nums -= lis[num_break]
        if nums == 0:
            break
        num_break -= 1
    print(sol, power - num_break)
