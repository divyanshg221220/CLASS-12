#2.10
def addDict(dict1,dict2):
    d={}
    for i in dict1:
        d[i]=dict1[i]
    for i in dict2:
        d[i]=dict2[i]
    return d
print(addDict(dict1=eval(input("Enter a dictionary: ")),
dict2=eval(input("Enter a dictionary: "))))
