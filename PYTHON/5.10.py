#5.10
def DISPLAYWORDS():
    f=open("STORY.TXT","r")
    for i in f.read().split():
        if len(i)<4:
            print(i)
    f.close()
DISPLAYWORDS()
