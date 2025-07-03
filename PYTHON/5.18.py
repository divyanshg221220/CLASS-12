#5.18
import pickle
def destination():    
    try:
        f=open("TRAIN.DAT","rb")
        while True:
            Train=pickle.load(f)
            if Train["To"]=="Delhi":
                print(Train)
                break
    except EOFError:
        f.close()
    except OSError:
        print("File not found")
destination()
