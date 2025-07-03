#3.9
def series(f,l):
    t=()
    s=(f+l)//4
    for i in range(f,l+1,s):
        t+=(i,)
    return t
f=int(input("Enter first value: "))
l=int(input("Enter last value: "))
print(series(f,l))
