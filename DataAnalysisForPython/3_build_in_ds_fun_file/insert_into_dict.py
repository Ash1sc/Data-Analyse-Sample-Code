import __init__
from collections import defaultdict

# insert into a empty dict
words = ["apple", "bat", "bar", "atom", "book"]

by_letter = {}


# use setdefault
for w in words:
    letter = w[0]
    by_letter.setdefault(letter, []).append(w)

for k, v in by_letter.items():
    print(f"key: {k}, value: {v}")

by_letter_2 = defaultdict(list)

# use default dicta
for w in words:
    by_letter_2[w[0]].append(w)
for k, v in by_letter_2.items():
    print(f"key: {k}, value: {v}")
