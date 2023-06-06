def main():
    num = int(input())
    if num % 100 < 49:
        num = max(num // 100, 1) * 100 - 1
    else:
        num = num // 100 * 100 + 99
    return num


print(main())