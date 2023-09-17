from sys import stdout
while True:
    n = int(input())
    if n == 0:
        break
    else:
        n -= 1
        v = []
        pointer = 1

        while n > 0:
            if n % 2 == 1:
                v.append(pointer)
            pointer *= 3
            n //= 2

        stdout.write("{ ")
        for i in range(len(v)):
            stdout.write(str(v[i]))
            if i != len(v) - 1:
                stdout.write(",")
            stdout.write(" ")
        stdout.write("}")
        stdout.write('\n')