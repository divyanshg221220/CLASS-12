#3.6
def nthRoot(x,n=2):
    return x**(1/n)
x=int(input("Enter a number: "))
while True:
    print("1. x^(1/n)")
    print("2. x^(1/2)")
    print("3. EXIT")
    print()
    choice=int(input("USER'S CHOICE: "))
    if choice==1:
        n=int(input("Enter a number: "))
        print(str(x)+"^(1/"+str(n)+")=",nthRoot(x,n))
    elif choice==2:
        print(str(x)+"^(1/2)=",nthRoot(x))
    elif choice==3:
        print("EXITED BY USER")
        break
    print()
