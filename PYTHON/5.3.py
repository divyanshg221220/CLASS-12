#5.3
f=open(input("Enter path of source file: "),"r")
print("Name\tTelephone number")
for i in f.readlines():
    print("\t".join(i.split()))
f.close()
