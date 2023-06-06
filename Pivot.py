'''
8
2 1 3 4 7 5 6 8
'''

num = int(input())
lis = input().split()
count = 0
max_left = int(lis[0])
mini_right = int(lis[-1])
max_lis = [0] * num
max_lis[0] = int(lis[0])
mini_lis = [0] * num
mini_lis[-1] = int(lis[-1])
for i in range(1, num):
    if int(lis[i]) > max_left:
        max_left = int(lis[i])
        max_lis[i] = int(lis[i])
    else:
        max_lis[i] = max_left

for i in range(num - 2, -1, -1):
    if int(lis[i]) < mini_right:
        mini_right = int(lis[i])
        mini_lis[i] = int(lis[i])
    else:
        mini_lis[i] = mini_right
for i in range(num):
    if i == 0:
        if int(lis[i]) < mini_lis[1]:
            count += 1
    elif i == num - 1:
        if int(lis[i]) > max_lis[num - 2]:
            count += 1
    elif mini_lis[i + 1] > int(lis[i]) > max_lis[i - 1]:
        count += 1
print(count)