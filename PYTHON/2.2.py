#2.2
l=[]
print("PRESS CTRL+C TO EXIT")
try:
    while True:
        l.append(input("enter "))
except KeyboardInterrupt:
    print("EXITED BY USER")
print()
for i in l:
    print(i,end="")
print()
print("1. Number of words")
print("2. Number of character")
print("3. Percentage of character that are alpha numeric")
print("4. EXIT")
print()
while True:
    choice=int(input("USER'S CHOICE: "))
    if choice==1:
        w=0
        for i in l:
            for j in i.split():
                w+=1
        print("Number of words:",w)
    elif choice==2:
        c=-1
        for i in l:
            c+=len(i)
        print("Number of character:",c)
    elif choice==3:
        c=-1
        a=0
        for i in l:
            c+=len(i)
            for j in i.split():
                if j.isalnum():
                    a+=len(j)
        print("Percentage of character that are alpha numeric:",a/c*100,"%")
    elif choice==4:
        print("EXITED BY USER")
        break
    print()
