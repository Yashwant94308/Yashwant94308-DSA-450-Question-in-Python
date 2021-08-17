words = ["cat", "map", "bat", "man", "pen"]
queries = ["?at", "ma?", "?a?", "??n"]


class TrieNode:
    def __init__(self):
        self.children = {}
        self.EndOfWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word):
        res = []

        def dfs(root, j, s):
            cur = root
            for i in range(j, len(word)):
                c = word[i]
                if c == '?':
                    for k, child in cur.children.items():
                        b, tr = dfs(child, i + 1, s + k)

                        if b is True:
                            res.append(tr)

                    return False, ''
                else:
                    if c not in cur.children:
                        return False, ''
                    s += c
                    cur = cur.children[c]
            return cur.endOfWord, s

        dfs(self.root, 0, '')
        print(res)


t = Trie()
for w in words:
    t.add(w)
for q in queries:
    t.search(q)
print()
