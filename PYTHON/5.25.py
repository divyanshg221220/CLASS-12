#5.25
import csv
def add():
    f=open("furdata.csv","a",newline="")
    w=csv.writer(f)
    fid=int(input("Enter furniture id : "))
    fname=input("Enter furniture name : ")
    fprice=float(input("Enter furniture price : "))
    w.writerow([fid,fname,fprice])
    f.close()
def search():
    f=open("furdata.csv","r",newline="")
    r=csv.reader(f)
    for i in r:
        if float(i[2])>10000:
            print(i[0],"\t",i[1],"\t",i[2])
    f.close()
while True:
    print("1. add()")
    print("2. search()")
    print("3. EXIT")
    print()
    choice=int(input("USER'S CHOICE: "))
    if choice==1:
        add()
    elif choice==2:
        search()
    elif choice==3:
        print("EXITED BY USER")
        break
    print()
