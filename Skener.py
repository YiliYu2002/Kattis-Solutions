'''
3 3 1 2
.x.
x.x
.x.
'''
line = input().split()
row = int(line[0])
col = int(line[1])
col_m = int(line[2])
row_m = int(line[3])
for i in range(row):
    str = input()
    temp = ''
    for j in range(len(str)):
        temp += str[j] * row_m
    for k in range(col_m):
        print(temp)

