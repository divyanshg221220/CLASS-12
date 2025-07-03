#5.5
def AMCount():
    f=open("STORY.TXT","r")
    txt=f.read()
    print("A or a :",txt.count("A")+txt.count("a"))
    print("M or m :",txt.count("M")+txt.count("m"))
    f.close()
AMCount()
