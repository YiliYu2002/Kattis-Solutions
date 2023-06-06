line = input()
sum = 0
for i in range(len(line)):
    sum += ord(line[i])
sum //= len(line)
print(chr(sum))
