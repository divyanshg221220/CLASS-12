#2.12
d=eval(input("Enter a dictionary: "))
l=list(d.values())
n=len(l)
for i in range(n):
    for j in range(0,n-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print("List of sorted values:",l)
