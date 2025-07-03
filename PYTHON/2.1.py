#2.1
n=input("Enter a phone number: ")
if len(n)==12 and n[3]=="-" and n[7]=="-" and (n[:3]+n[4:7]+n[8:]).isdigit():
    print("Valid format")
else:
    print("Invalid format")
