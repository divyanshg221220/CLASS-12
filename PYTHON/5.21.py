#5.21
import csv
f=open(input("Enter file name : "),"r",newline="")
r=csv.reader(f,delimiter="\t")
for i in r:
    print(i)
f.close()
