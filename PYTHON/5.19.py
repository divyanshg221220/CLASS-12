#5.19
import pickle
def CreateFile():
    f=open("Book.dat","ab")
    print("PRESS CTRL+C TO EXIT")
    try:
        while True:
            pickle.dump([int(input("BookNo: ")),input("Book_Name: "),input("Author: "),int(input("Price: "))],f)
            print()
    except KeyboardInterrupt:
        f.close()
        print("EXITED BY USER")
def CountRec(Author):
    import pickle
    try:
        f=open("Book.dat","rb")
        c=0
        while True:
            book=pickle.load(f)
            if book[2]==Author:
                c+=1
    except EOFError:
        f.close()
        print(c)
    except OSError:
        print("File not found")
while True:
    print("1. CreateFile()")
    print("2. CountRec(Author)")
    print("3. EXIT")
    print()
    choice=int(input("USER'S CHOICE: "))
    if choice==1:
        CreateFile()
    elif choice==2:
        CountRec(input("Author: "))
    elif choice==3:
        print("EXITED BY USER")
        break
