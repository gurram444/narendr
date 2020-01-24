from collections import OrderedDict

words = OrderedDict()

for _ in range(int(input())):
    key = input()
    if key in words:
        words[key] += 1
    else:
        words[key] = 1
print(len(words))
print (' '.join(map(str, words.values())))
