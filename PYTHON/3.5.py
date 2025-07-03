#3.5
def length_check(n,m):
    if len(n)==len(m):
        return True
    else:
        return False
print(length_check(input("Enter a string: "),input("Enter a string: ")))
