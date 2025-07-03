#5.2
def atheletic():
    import pickle
    f1=open("sports.dat","rb")
    f2=open("Atheletic.dat","wb")
    try:
        while True:
            str=pickle.load(f1)
            if str.startswith("Atheletics"):
                pickle.dump(str,f2)
    except EOFError:
        f1.close()
        f2.close()
    except OSError:
        print("File not found")
atheletic()
