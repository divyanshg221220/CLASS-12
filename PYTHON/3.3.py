#3.3
def cube(n=2):
    print(n**3)
def equal(char1,char2):
    if char1==char2:
        return True
    else:
        return False
while True:
    print("1. cube(n=2)")
    print("2. equal(char1,char2)")
    print("3. EXIT")
    print()
    choice=int(input("USER'S CHOICE: "))
    if choice==1:
        try:
            n=int(input("Enter a number: "))
            cube(n)
        except:
            cube()
    elif choice==2:
        print(equal(char1=input("Enter a character: "),char2=input("Enter a character: ")))
    elif choice==3:
        print("EXITED BY USER")
        break
    print()
