#1.7
N=int(input("Enter an integer: "))
s=0
if N>0:
    for i in range(N,(2*N)+1):
        s+=i
    print("Sum of integer between N and 2*N is:",s)
elif N<0:
    for i in range(2*N,N+1):
        s+=i
    print("Sum of integer between 2*N and N is:",s)
