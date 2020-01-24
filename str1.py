st='i am narendra'            #reverse a string word by word
st1=st.split()
print(st1)
st2=reversed(st1)
op=' '.join(st2)
print(op)
st4=reversed(st1[0])
p=''.join(st4)
print(p)
st3=reversed(st1[1])
op1=''.join(st3)

print(op1)



class narendra:      #uppercase

    def __init__(self,str):
        self.str=str
    def print_string(self):
        print(str.upper(self.str))

st=narendra('narendra')
st.print_string()

