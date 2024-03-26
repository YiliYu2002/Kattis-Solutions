#
#
#
# def convert(c):
#     return {'0': ' ', '<': ',', '>': '.'}[c]
#
#
# def correct(s):
#     if s == '!':
#         return s.replace('!', '-.')
#     return s
#
#
# s, a = input().split()
# offset = sum(map(lambda x: ord(x) - 32, correct(s))) - ord(a)
# for line in sys.stdin:
#     line = line.strip().split()
#     print(''.join(map(lambda x: chr(sum(map(lambda y: ord(y) - 32, correct(x))) - offset) if x not in ['0', '>',
#                                                                                                        '<'] else convert(
#         x), line)))
# import sys
# s, a = input().split()
# offset = sum(map(lambda x: ord(x) - 32, correct(s))) - ord(a)
# dic = {'0': ' ', '<': ',', '>': '.'}
# for line in sys.stdin:
#     sol = ''
#     line = line.strip().split()
#     for i in line:
#         if i in dic:
#         else:
#             if i == '!':
#                 sol += '-.'

# import sys
#
#
# # Function to calculate the offset
# def calculate_offset(s, a):
#     return sum(ord(char) - 32 for char in correct(s)) - ord(a)
#
#
# def convert(c):
#     return {'0': ' ', '<': ',', '>': '.'}[c]
#
#
# def correct(s):
#     return s if s != '!' else s.replace('!', '-.')
#
#
# # Function to process a line
# def process_line(line, offset):
#     t = line.strip().split()
#     res = []
#     for word in t:
#         if word not in ['0', '>', '<']:
#             sol = chr(sum(ord(char) - 32 for char in correct(word)) - offset)
#             res.append(sol)
#         else:
#             res.append(convert(word))
#     return ''.join(res)
#
#
# # Your original code
# s, a = input().split()
# offset = calculate_offset(s, a)
#
# for line in sys.stdin:
#     transformed_line = process_line(line, offset)
#     print(transformed_line)
import sys


def score_rune(rune):
    first = ord('!')
    score = 0

    for ch in rune:
        score += ord(ch) - first + 1

    return score


def decode_rune(rune, offset):
    score = score_rune(rune)
    code = ord('a') - offset - 1 + score

    if code < ord('a'):
        code += 26
    elif code > ord('z'):
        code -= 26

    return chr(code)


header = input().split()
rune = header[0]
letter = header[1]

rune_score = score_rune(rune)
offset = rune_score - (ord(letter) - ord('a') + 1)

for line in sys.stdin:
    runes = line.strip().split(' ')
    for rune in runes:
        if rune == "0":
            print(" ", end="")
        elif rune == "<":
            print(",", end="")
        elif rune == ">":
            print(".", end="")
        else:
            letter = decode_rune(rune, offset)
            print(letter, end="")
    print("")