#4.3
import massconversion
while True:
    print("1. kgtotonne()")
    print("2. tonnetokg()")
    print("3. kgtopound()")
    print("4. poundtokg()")
    print("5. help()")
    print("6. EXIT")
    print()
    choice=int(input("USER'S CHOICE: "))
    if choice==1:
        print("tonne:",massconversion.kgtotonne(int(input("Enter value in kilogram: "))))
    elif choice==2:
        print("kilogram:",massconversion.tonnetokg(int(input("Enter value in tonne: "))))
    elif choice==3:
        print("pound:",massconversion.kgtopound(int(input("Enter value in kilogram: "))))
    elif choice==4:
        print("kilogram:",massconversion.poundtokg(int(input("Enter value in pound: "))))
    elif choice==5:
        print(massconversion.help())
    elif choice==6:
        print("EXITED BY USER")
        break
    print()
