#8.1
def find_in_list(lst,v):
    for i in lst:
        if v==i:
            print(lst.index(i))
            break
    else:
        print(-1)
lst=eval(input("Enter a list : "))
v=eval(input("Enter a value : "))
find_in_list(lst,v)
