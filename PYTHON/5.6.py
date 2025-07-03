#5.6
f=open("Article.txt","r")
txt=f.read()
c=0
for i in txt:
    if i.isupper():
        c+=1
print(c)
f.close()
