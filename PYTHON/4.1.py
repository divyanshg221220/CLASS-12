#4.1
def remove_letter(sentence,letter):
    return "".join(sentence.split(letter))
def capwords(sentence):
    s=""
    for i in sentence.split(" "):
        s+="".join(i.capitalize())+" "
    return sentence,s
while True:
    print("1. remove_letter(sentence,letter)")
    print("2. capwords()")
    print("3. EXIT")
    print()
    choice=int(input("USER'S CHOICE: "))
    if choice!=3:
        sentence=input("Enter a string: ")
    if choice==1:
        letter=input("Enter a string: ")
        print(remove_letter(sentence,letter))
    elif choice==2:
        o,n=capwords(sentence)
        print("Before change:",o)
        print("After change:",n)
    elif choice==3:
        print("EXITED BY USER")
        break
    print()
