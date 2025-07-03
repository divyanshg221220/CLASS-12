#5.11
f1=open("LOWER.TXT","w")
f2=open("UPPER.TXT","w")
f3=open("OTHERS.TXT","w")
print("PRESS CTRL+C TO EXIT")
try:
    while True:
        str=input("Enter a character : ")
        if str.islower():
            f1.write(str)
        elif str.isupper():
            f2.write(str)
        else:
            f3.write(str)
except KeyboardInterrupt:
    f1.close()
    f2.close()
    f3.close()
    print("EXITED BY USER")
