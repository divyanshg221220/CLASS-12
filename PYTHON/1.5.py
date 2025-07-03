#1.5
nd={1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday",7:"Sunday"}
dn={"Monday":1,"Tuesday":2,"Wednesday":3,"Thursday":4,"Friday":5,"Saturday":6,"Sunday":7}
n=int(input("Enter a number between 2 to 365: "))
while 2>=n or n>=365:
    n=int(input("Enter a number between 2 to 365: "))
day=input("Enter first day of the year: ")
n+=dn[day]
n%=7
if n==0:
    n=7
print(nd[n-1])
