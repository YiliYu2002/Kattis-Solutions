import sys
from bisect import bisect_right


class TrieNode:

    # Trie node class
    def __init__(self):
        self.children = [None] * 26
        self.wordIndices = []

        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False


class Trie:

    # Trie data structure class
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):

        # Returns new trie node (initialized to NULLs)
        return TrieNode()

    def _charToIndex(self, ch):

        # private helper function
        # Converts key current character into index
        # use only 'a' through 'z' and lower case

        return ord(ch) - ord('a')

    def insert(self, key, wordIndex):

        # If not present, inserts key into trie
        # If the key is prefix of trie node,
        # just marks leaf node
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])

            # if current character is not present
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]
            pCrawl.wordIndices.append(wordIndex)

        # mark last node as leaf
        pCrawl.isEndOfWord = wordIndex

    def search(self, key):

        # Search key in the trie
        # Returns true if key presents
        # in trie, else false
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]

        return pCrawl.isEndOfWord

    def cost(self, key, wordIndex=40000):

        cost = wordIndex + 1
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return cost
            pCrawl = pCrawl.children[index]
            cost += bisect_right(pCrawl.wordIndices, wordIndex)

        return cost


# wordlist = {}
# T = Trie()
# n = int(input())
# for i in range(n):
#     s = input()
#     wordlist[s] = i
#     T.insert(s, i)
#
# Q = int(input())
# for _ in range(Q):
#     query = input()
#     if query in wordlist:
#         print(T.cost(query, wordlist[query]))
#     else:
#         print(T.cost(query, n - 1))

# for line in sys.stdin:
while True:
    sol = ''
    try:
        line = input()
    except EOFError:
        break
    case = input()
    l = 0
    le = len(line)
    while True:
        t = case.find(line, l)
        # print(t)
        if t == -1:
            break
        else:
            l = t + 1
            print(t, end=' ')
            if l >= len(case):
                break
    print('')

# for line in sys.stdin:
#     sol = ''
#     # line = input()
#     case = input()
#     l = 0
#     le = len(line)
#     while True:
#         t = case.find(line, l)
#         # print(t)
#         if t == -1:
#             break
#         else:
#             l = t + le
#             sol += ' ' + str(t)
#         if l >= len(case):
#             break
#     print(sol[1:]) if len(sol) > 1 else print(sol)