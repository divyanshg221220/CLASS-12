#3.8
def min_ones_digit(n,m):
    if int(str(n)[-1])<int(str(m)[-1]):
        return n
    elif int(str(n)[-1])>int(str(m)[-1]):
        return m
print(min_ones_digit(int(input("Enter a number: ")),int(input("Enter a number: "))))
