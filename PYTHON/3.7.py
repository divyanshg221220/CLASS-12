#3.7
import random
def random_number(n):
    s=""
    for i in range(n):
        if i==0:
            s+=str(random.randint(1,9))
        else:
            s+=str(random.randint(0,9))
    return s
print(random_number(int(input("Enter a number: "))))
