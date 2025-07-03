#5.20
def Show_words():
    try:
        f=open("NOTES.TXT","r")
        for i in f.readlines():
            if len(i.split())==5:
                print(i)
    except IOError:
        print("File not found")
Show_words()
