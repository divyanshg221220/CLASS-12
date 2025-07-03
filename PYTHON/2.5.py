#2.5
l=eval(input("Enter a list: "))
m=0
for i in range(len(l)):
    if len(l[i])>m:
        m=i
print(l[i])
