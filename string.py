def char_frequency(str1):             # count of each character
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency('narendra'))


def len_string(str):                   # finding the length of the string, list and tuple
    count=0
    for i in str:
        count +=1
    return count
print(len_string('narendra'))

