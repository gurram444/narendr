from collections import OrderedDict             # word order
words = OrderedDict()

for _ in range(int(input())):
    key = input()
    if key in words:
        words[key] += 1
    else:
        words[key] = 1
print(len(words))
print (' '.join(map(str, words.values())))


def minion_game(s):                        #minion_game

    vowels = 'AEIOU'
    kevsc = 0
    stusc = 0
    for i in range(len(s)):
        if s[i] in vowels:
            kevsc += (len(s)-i)
        else:
            stusc += (len(s)-i)

    if kevsc > stusc:
        print ("Kevin", kevsc)
    elif kevsc < stusc:
        print ("Stuart", stusc)
    else:
        print ("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)


import textwrap                       #textwrap
def wrap(string, max_width):
    return "\n".join([string[i:i + max_width] for i in range(0, len(string), max_width)])

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

import operator                     # decorators 2- name directory
def person_lister(f):
    def inner(people):
        # complete the function
        return map(f,sorted(people, key=lambda x: int(x[2])))
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')


cube=lambda x:x**3          # fibonacci and lambda function

def fibonacci(n):
    initiallist=[]
    for i in range(n):
        if i<2:
            initiallist +=[i]
        else:
            initiallist +=[initiallist[-1]+initiallist[-2]]
    return initiallist

n=int(input())
print(list(map(cube,fibonacci(n))))