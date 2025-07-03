#2.9
d={"January":31,"February":28,"March":31,"April":30,"May":31,"June":30,"July":31,"August":31,
"September":30,"October":31,"November":30,"December":31}
while True:
    print("1. Number of days")
    print("2. Name of months in alphabetical order")
    print("3. Name of months with 31 days")
    print("4. Name of months in numerical order")
    print("5. EXIT")
    print()
    choice=int(input("USER'S CHOICE: "))
    if choice==1:
        print("Number of days:",d[input("Name of month: ")])
    elif choice==2:
        print("Name of months in alphabetical order:")
        l=list(d.keys())
        l.sort()
        for i in l:
            print(i)
    elif choice==3:
        print("Name of months with 31 days: ")
        for i in d:
            if d[i]==31:
                print(i)
    elif choice==4:
        print("Name of months in numerical order:")
        for i in d:
            if d[i]==28:
                print(i,"-",d[i])
        for i in d:
            if d[i]==30:
                print(i,"-",d[i])
        for i in d:
            if d[i]==31:
                print(i,"-",d[i])
    elif choice==5:
        print("EXITED BY USER")
        break
    print()
