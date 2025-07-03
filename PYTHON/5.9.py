#5.9
f=open("MYNOTES.TXT","r")
for i in f.readlines():
    if i[0]=="K":
        print(i)
f.close()
