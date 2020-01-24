myset={1,2,3,4,5,6}
print(myset)
myset.discard(4)
print(myset)
myset.remove(5)
print(myset)

set={2,4,5,8,9,6}
s={1,2,3,4,5,6}
print(set.intersection(s))


with open('nani.txt','r') as f:
    with open('out.txt','w') as f1:
        for line in f:
            f1.write(line)
        print("successfully write program")
    f1.close()
f.close()