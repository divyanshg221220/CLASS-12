#5.17
import pickle
try:
    f=open("COMPANY.DAT","rb")
    while True:
        Company=pickle.load(f)
        if Company["CompID"]=="1005":
            print(Company)
            break
except EOFError:
    f.close()
except OSError:
    print("File not found")
