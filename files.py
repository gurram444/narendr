import json                       #creating json file
data={}
data['people']=[]
data['people'].append({'name':'scott','website':'facebook.com','from':'america'})
data['people'].append({'name':'larry','website':'google.com','from':'india'})
data['people'].append({'name':'john','website':'apple.com','from':'alabama'})
file=open('data.json','w')
json.dump(data,file)
file.close()


json_file=open('data.json')      #reading data from the json
data=json.load(json_file)
json_file.close()
lst=data['people']
for p in lst:
    print('name:' +p['name'])
    print('website:' +p['website'])
    print('from:' +p['from'])


f=open("abcd.txt",'w')     #writing data into file
f.write("Durga\n")
f.write("Software\n")
f.write("Solutions\n")
print("Data written to the file successfully")
f.close()

f = open("abc.txt", 'w')     # various properties of file
print("File Name: ", f.name)
print("File Mode: ", f.mode)
print("Is File Readable:  ", f.readable())
print("Is File Writable:  ", f.writable())
print("Is File Closed : ", f.closed)
f.close()
print("Is File Closed : ", f.closed)


f=open("abc.txt",'w')        # writing lines into file
list=["sunny\n","bunny\n","vinny\n","chinny"]
f.writelines(list)
print("List of lines written to the file successfully")
f.close()

f=open("abc.txt",'r')     #reading all the data
data=f.read()
print(data)
f.close()

f=open("abc.txt",'r')     # reading only first n characters from file
data=f.read(10)
print(data)
f.close()

f=open("abc.txt",'r')     # reading line by line
line1=f.readline()
print(line1,end='')
line2=f.readline()
print(line2,end='')
line3=f.readline()
print(line3,end='')
f.close()

import os,sys         #check given file exists or not if it is exist read data
fname=input("Enter File Name: ")
if os.path.isfile(fname):
    print("File exists:",fname)
    f=open(fname,"r")
else:
    print("File does not exist:",fname)
    sys.exit(0)
print("The content of file is:")
data=f.read()
print(data)