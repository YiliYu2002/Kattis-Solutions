num_line = int(input())
for i in range(num_line):
    num_num_line = input().split()
    num_num = int(num_num_line[0])
    temp = 1
    for j in range(2, num_num):
        if int(num_num_line[j]) != int(num_num_line[temp]) + 1:
            temp += 1
            break
        else:
            temp += 1
    print(temp)
