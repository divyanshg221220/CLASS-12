#4.2
import lengthconversion
while True:
    print("1. miletokm()")
    print("2. kmtomile()")
    print("3. feettoinches()")
    print("4. inchestofeet()")
    print("5. help()")
    print("6. EXIT")
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
        print("EXITED BY USER")
        break
    print()
