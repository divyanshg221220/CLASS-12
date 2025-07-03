#2.3
L=eval(input("Enter a list: "))
M=eval(input("Enter a list: "))
N=[]
for i in range(len(L)):
    N.append(L[i]+M[i])
print(N)
