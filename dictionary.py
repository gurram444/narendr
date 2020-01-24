x={'java':80,'python':90,'aws':70,'devops':75}
print(x)
print(x.get('aws'))
print(x['python'])
x['aws']=85
x['hadoop']=82
print(x)
for p in x:
    print(p,x[p])

k=x.keys()
for p in k:
    print(p)
v=x.values()
for q in v:
    print(q)

kv=x.items()
for k,v in kv:
    print(k,v)
    
for i in kv:
    print(i[0],i[1])

n=[l for l,v in x.items() if v==90]
print(n)
print(sorted(x.items(),key= lambda kv:(kv[1],kv[0])))    #sorted dict by using values
print(sorted(x.items()))


data={'a':1,'b':2,"c":3}
d={}
for k,v in data.items():
    if v in d:
        d[v].append(k)
    else:
        d[v]=[k]
print("k:v")
for j in d:
    print(j, ":",d[j])
