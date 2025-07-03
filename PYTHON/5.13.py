#5.13
f=open(input("Enter path of source file: "),"r")
str=f.read()
print(len(str[:str.index("$")]))
f.close()
