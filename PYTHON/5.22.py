#5.22
import csv
fn=input("Enter file name : ")
f=open(fn,"w",newline="")
w=csv.writer(f)
rdata=[]
m,n=int(input("Enter number of rows : ")),int(input("Enter number of columns : "))
for i in range(m):
    cdata=[]
    for j in range(n):
        cdata.append(input("Enter data : "))
    rdata.append(cdata)
w.writerows(rdata)
f.close()
f=open(fn,"r",newline="")
r=csv.reader(f)
for i in r:
    print(i)
f.close()
