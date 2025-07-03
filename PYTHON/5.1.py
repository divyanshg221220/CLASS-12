#5.1
f1=open(input("Enter path of source file: "),"r")
f2=open(input("Enter path of destination file: "),"w")
for i in f1.readlines():
    f2.write(" ".join(i.split())+"\n")
f1.close()
f2.close()
