#5.23
import csv
def replace():
    f=open(input("Enter old file name : "),"r",newline="")
    r=csv.reader(f,delimiter=input("Enter old element : "))
    data=[]
    for i in r:
        data.append(i)
    f.close()
    f=open(input("Enter new file name : "),"w",newline="")
    w=csv.writer(f,delimiter=input("Enter new element : "))
    w.writerows(data)
    f.close()
replace()
