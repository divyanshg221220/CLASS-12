#5.16
import pickle
try:
    f=open("staff.dat","rb")
    while True:
        Staff=pickle.load(f)
        if Staff["Staffcode"]=="S0105":
            print(Staff)
            break
except EOFError:
    f.close()
except OSError:
    print("File not found")
