#5.4
f=open("Poem.txt","r")
txt=f.read().split()
print("to :",txt.count("to"))
print("the :",txt.count("the"))
f.close()
