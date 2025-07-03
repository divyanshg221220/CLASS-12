#3.4
import random
def random_range(n,m):
    for i in range(3):
        print(random.randint(n,m))
random_range(int(input("Enter first value: ")),int(input("Enter last value: ")))
