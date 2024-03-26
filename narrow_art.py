# import math
# while True:
#     n, k = map(int, input().split())
#     if n == 0 and k == 0:
#         exit()
#     dp = [[[0 for _ in range(k + 1)] for _ in range(3)] for _ in range(n)]
#     g = [[0 for _ in range(2)]for _ in range(n)]
#
#     for i in range(n):
#         g[i][0], g[i][1] = map(int, input().split())
#
#     for i in range(3):
#         for j in range(k + 1):
#             dp[0][i][j] = -math.inf
#
#     dp[0][0][0] = g[0][0] + g[0][1]
#     dp[0][1][1] = g[0][1]
#     dp[0][2][1] = g[0][0]
#
#     for i in range(1, n):
#         for j in range(k + 1):
#             dp[i][0][j] = max(dp[i-1][0][j], max(dp[i-1][1][j], dp[i-1][2][j])) + g[i][0] + g[i][1]
#             if j != 0:
#                 dp[i][1][j] = max(dp[i-1][0][j-1], dp[i-1][1][j-1]) + g[i][1]
#                 dp[i][2][j] = max(dp[i-1][0][j-1], dp[i-1][2][j-1]) + g[i][0]
#
#     print(max(dp[n-1][0][k], max(dp[n-1][1][k], dp[n-1][2][k])))

# def count(a, i, b):
#     res = 0
#     j = 0
#     while i < len(a) and j < len(b):
#         if a[i] != b[j]:
#             return 0
#         i += 1
#         j += 1
#         res += 1
#     return res
#
#
# def check(a, b, l):
#     res = 0
#     for i in range(len(a)):
#         res = count(a, i, b)
#         if res:
#             break
#     return l - res
#
#
# case = int(input())
# for _ in range(case):
#     l, n = map(int, input().split())
#     res = 0
#     sol = ''
#     i = 0
#     while i < n:
#         line = input()
#         res += check(sol, line, l)
#         sol = line
#         i += 1
#     print(res)

# def longest_repeating_substring_length(s):
#     def has_repeating_substring(s, length):
#         seen = set()
#         for i in range(len(s) - length + 1):
#             substring = s[i:i + length]
#             if substring in seen:
#                 return True
#             seen.add(substring)
#         return False
#
#     # Binary search for the length of the repeating substring
#     left, right = 1, len(s)
#     longest_length = 0
#
#     while left <= right:
#         mid = left + (right - left) // 2
#         if has_repeating_substring(s, mid):
#             longest_length = mid
#             left = mid + 1
#         else:
#             right = mid - 1
#
#     return longest_length

# def longest_repeating_substring_length(s):
#     def check_length(length):
#         base = 26  # Assuming lowercase English alphabet
#         modulus = 2 ** 64  # A large prime number
#
#         # Calculate hash for the first substring of length 'length'
#         hash_value = 0
#         base_power_length = 1
#         for i in range(length):
#             hash_value = (hash_value * base + ord(s[i])) % modulus
#             if i < length - 1:
#                 base_power_length = (base_power_length * base) % modulus
#
#         seen = {hash_value}
#
#         for i in range(length, len(s)):
#             # Update hash using rolling hash
#             hash_value = (hash_value * base - ord(s[i - length]) * base_power_length + ord(s[i])) % modulus
#             if hash_value in seen:
#                 return True
#             seen.add(hash_value)
#
#         return False
#
#     # Binary search for the length of the repeating substring
#     left, right = 1, len(s)
#     longest_length = 0
#
#     while left <= right:
#         mid = left + (right - left) // 2
#         if check_length(mid):
#             longest_length = mid
#             left = mid + 1
#         else:
#             right = mid - 1
#
#     return longest_length
from bisect import bisect_right

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.indices = []

class Trie:
    def __init__(self):
        self.root = self.get_node()

    def get_node(self):
        return TrieNode()

    def _char_to_index(self, ch):
        return ord(ch) - ord('a')

    def insert(self, key, index):
        p_crawl = self.root
        length = len(key)
        for level in range(length):
            index = self._char_to_index(key[level])
            if not p_crawl.children[index]:
                p_crawl.children[index] = self.get_node()
            p_crawl = p_crawl.children[index]
            p_crawl.indices.append(index)

    def longest_repeating_substring(self):
        max_length = 0
        p_crawl = self.root
        for child in p_crawl.children:
            if child:
                max_length = max(max_length, len(child.indices))
        return max_length

# Function to find the length of the longest repeating substring
def longest_repeating_substring_length(s):
    trie = Trie()
    for i in range(len(s)):
        trie.insert(s[i:], i)

    return trie.longest_repeating_substring()


l = input()
print(longest_repeating_substring_length(input())-1)
