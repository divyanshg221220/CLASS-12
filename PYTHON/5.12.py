#5.12
def count_display():
    f=open("LINES.TXT","r")
    c=0
    for i in f.readlines():
        if i[0]=="A":
            print(i,end="")
            c+=1
    print("\nCount :",c)
    f.close()
count_display()
