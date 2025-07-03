#3.2
def volume(length_of_box=1,width_of_box=1,height_of_box=1):
    print(length_of_box*width_of_box*height_of_box,"unit^3")
while True:
    print("1. length of box")
    print("2. width of box")
    print("3. height of box")
    print("4. EXIT")
    print()
    choice=int(input("USER'S CHOICE: "))
    if choice==1:
        volume(length_of_box=float(input("Enter length of box: ")))
    elif choice==2:
        volume(width_of_box=float(input("Enter width of box: ")))
    elif choice==3:
        volume(height_of_box=float(input("Enter height of box: ")))
    elif choice==4:
        print("EXITED BY USER")
        break
    print()
