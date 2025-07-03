#1.6
def inch(f):
    i=f*12
    return i
def feet():
    f=int(input("Enter number of feet: "))
    return f
def display(i):
    print("Number of inches is:",i)
display(inch(feet()))
