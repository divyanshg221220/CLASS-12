#5.7
f1=open(input("Enter path of source file: "),"r")
f2=open(input("Enter path of destination file: "),"w")
f2.write(f1.read())
f1.close()
f2.close()
