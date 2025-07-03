#1.8
i=int(input("Enter date : "))
i=str(i)
if len(i)!=8:
    i="0"+i
def format(i):
    n={1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",
9:"September",10:"October",11:"November",12:"December"}
    m=int(i[:2])
    d=int(i[2:4])
    y=int(i[4:])
    print(n[m],d,",",y)
format(i)
