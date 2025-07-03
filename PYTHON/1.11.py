#1.11
f=input("Please enter the first time : ")
s=input("Please enter the second time : ")
fh=int(f[:-2])
fm=int(f[-2:])
sh=int(s[:-2])
sm=int(s[-2:])
dh=sh-fh
dm=sm-fm
print(dh,"hours",dm,"minutes")
