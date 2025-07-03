#2.8
a=0
b=1
t=(a,)
for i in range(8):
    c=a+b
    a=b
    b=c
    t+=(a,)
print(t)
