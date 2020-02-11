n=10
print(list(map(lambda x:x*5,range(1,n+1))))


def reverse_sentence(input_str):
    words = input_str.split(" ")
    newWords = [word[::-1] for word in words]
    newSentence = " ".join(newWords)

    return newSentence
input_str= input('input:')
print(reverse_sentence(input_str) )