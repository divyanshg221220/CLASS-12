#2.9
d={"January":31,"February":28,"March":31,"April":30,"May":31,"June":30,"July":31,"August":31,"September":30,"October":31,"November":30,"December":31}
while True:
    print("1. Ask the user to enter a month name and use the dictionary to tell them how many days are in that month.")
    print("2. Print out all of the keys in alphabetical order.")
    print("3. Print out the of months with 31 days.")
    print("4. Print out the (key-value) pairs sorted by the number of days in each month.")
    print("5. EXIT")
    print()
    choice=int(input("USER'S CHOICE:"))
    if choice==1:
        print("Number of days:",d[input("Name of month:")])
    elif choice==2:
        print("Name of months in alphabetical order:")
        l=list(d.keys())
        l.sort()
        for i in l:
            print(i)
    elif choice==3:
        print("Name of months with 31 days:")
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
