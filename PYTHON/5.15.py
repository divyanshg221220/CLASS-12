#5.15
import pickle
f=open("member.dat","wb")
Member={}
for i in range(int(input("Enter number of members : "))):
    Member["MemberNo."]=int(input("Enter member number : "))
    Member["Name"]=input("Enter member name : ")
    pickle.dump(Member,f)
f.close()
