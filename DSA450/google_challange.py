from collections import defaultdict
from functools import reduce

M = 3
words = ["cat", "map", "bat", "man", "pen"]
queries = ["?at", "ma?", "?a?", "??n"]

sets = defaultdict(set)
# print(sets)
for word in words:
    for i, c in enumerate(word):
        sets[i, c].add(word)

# print(sets)
all_words = set(words)

for q in queries:
    possible_words = (sets[i, c] for i, c in enumerate(q) if c != "?")

    w = reduce(set.intersection, possible_words, all_words)
    print(q, len(w), w)
