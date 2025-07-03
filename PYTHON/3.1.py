#3.1
while True:
    print("1. void_conversion(amount_in_dollars,dollar_to_rupee)")
    print("2. non_void_conversion(amount_in_dollars,dollar_to_rupee)")
    print("3. EXIT")
    print()
    choice=int(input("USER'S CHOICE: "))
    if choice==1:
        def void_conversion(amount_in_dollars,dollar_to_rupee):
            print("Rs.",amount_in_dollars*dollar_to_rupee)
        void_conversion(amount_in_dollars=float(input("amount-in-dollars: ")),
                        dollar_to_rupee=float(input("dollar-to-rupee: ")))
    elif choice==2:
        def non_void_conversion(amount_in_dollars,dollar_to_rupee):
            return amount_in_dollars*dollar_to_rupee
        print("Rs.",non_void_conversion(amount_in_dollars=float(input("amount-in-dollars: ")),
                                        dollar_to_rupee=float(input("dollar-to-rupee: "))))
    elif choice==3:
        print("EXITED BY USER")
        break
    print()
