import lengthconversion,massconversion
while True:
    print("1. miletokm()")
    print("2. kmtomile()")
    print("3. feettoinches()")
    print("4. inchestofeet()")
    print("5. help(lenthconversion)")
    print("6. kgtotonne()")
    print("7. tonnetokg()")
    print("8. kgtopound()")
    print("9. poundtokg()")
    print("10. help(massconversion)")
    print("11. EXIT")
    print()
    choice=int(input("USER'S CHOICE: "))
    if choice==1:
        print("km:",lengthconversion.miletokm(int(input("Enter value in mile: "))))
    elif choice==2:
        print("mile:",lengthconversion.kmtomile(int(input("Enter value in kilometer: "))))
    elif choice==3:
        print("inch:",lengthconversion.feettoinches(int(input("Enter value in feet: "))))
    elif choice==4:
        print("foot",lengthconversion.inchestofeet(int(input("Enter value in inch: "))))
    elif choice==5:
        print(lengthconversion.help())
    elif choice==6:
        print("tonne:",massconversion.kgtotonne(int(input("Enter value in kilogram: "))))
    elif choice==7:
        print("kilogram:",massconversion.tonnetokg(int(input("Enter value in tonne: "))))
    elif choice==8:
        print("pound:",massconversion.kgtopound(int(input("Enter value in kilogram: "))))
    elif choice==9:
        print("kilogram:",massconversion.poundtokg(int(input("Enter value in pound: "))))
    elif choice==10:
        print(massconversion.help())
    elif choice==11:
        print("EXITED BY USER")
        break
    print()
