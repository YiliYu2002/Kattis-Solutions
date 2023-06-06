def main():
    num = int(input())
    flag = True
    count = 1
    wordlist = {}
    a = input()
    wordlist[a] = 1
    a = a[-1]
    for i in range(1, num):
        word = input()
        if wordlist.get(word) is not None:
            count += 1
            flag = False
            break
        else:
            wordlist[word] = 1
            b = word[0]
            if a != b:
                count += 1
                flag = False
                break
            else:
                count += 1
                a = word[-1]

    if flag:
        return "Fair Game"
    else:
        if count % 2 == 1:
            return "Player 1 lost"
        else:
            return "Player 2 lost"


print(main())



