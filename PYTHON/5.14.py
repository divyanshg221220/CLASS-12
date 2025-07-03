#5.14
filout=open("STRS.txt","w")
print("PRESS CTRL+C TO EXIT")
try:
    while True:
        str=input("Enter a string : ")
        filout.write(str+"\n")
except KeyboardInterrupt:
    filout.close()
    print("EXITED BY USER")
