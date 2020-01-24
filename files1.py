import os,sys         # number of lines,words and characters in file
fname=input("Enter File Name: ")
if os.path.isfile(fname):
    print("File exists:",fname)
    f=open(fname,"r")
else:
    print("File does not exist:",fname)
    sys.exit(0)
lcount=wcount=ccount=0
for line in f:
    lcount=lcount+1
    ccount=ccount+len(line)
    words=line.split()
    wcount=wcount+len(words)
print("The number of Lines:",lcount)
print("The number of Words:",wcount)
print("The number of Characters:",ccount)


import csv                # writing data into csv files
with open("emp.csv","w",newline='') as f:
    w=csv.writer(f)   # returns csv writer object
    w.writerow(["ENO","ENAME","ESAL","EADDR"])
    n=int(input("Enter Number of Employees:"))
    for i in range(n):
        eno=input("Enter Employee No:")
        ename=input("Enter Employee Name:")
        esal=input("Enter Employee Salary:")
        eaddr=input("Enter Employee Address:")
        w.writerow([eno,ename,esal,eaddr])
print("Total Employees data written to csv file successfully")


import csv                   # reading data from csv files
f=open("emp.csv",'r')
r=csv.reader(f) #returns csv reader object
data=list(r)
#print(data)
for line in data:
    for word in line:
        print(word,"\t",end='')
    print()