#5.24
import csv
def replace():
    f=open(input("Enter old file name : "),"r",newline="")
    r=csv.reader(f,delimiter=",")
    data=[]
    for i in r:
        data.append(["check"]+i)
    f.close()
    f=open(input("Enter new file name : "),"w",newline="")
    w=csv.writer(f,delimiter=",")
    w.writerows(data)
    f.close()
replace()
