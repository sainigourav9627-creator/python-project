ATM_PIN = 1234
pin = int(input("Enter ATM PIN: "))

if pin == ATM_PIN:

    Current_Balance = 1000

    while True:

        print("===== ATM =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("Enter Choice: "))

        if choice == 1:
            print("Current Balance =", Current_Balance)

        elif choice == 2:
            amount = int(input("Enter Deposit Amount: "))

            if amount > 0:
                Current_Balance = Current_Balance + amount
                print("Current Balance =", Current_Balance)
            else:
                print("Invalid Amount")

        elif choice == 3:
            amount = int(input("Enter Withdraw Amount: "))

            if amount > 0:

                if amount <= Current_Balance:
                    Current_Balance = Current_Balance - amount
                    print("Current Balance =", Current_Balance)

                else:
                    print("Insufficient Balance")

            else:
                print("Invalid Amount")

        elif choice == 4:
            print("Thank You")
            break

        else:
            print("Invalid Choice")

else:
    print("Wrong PIN")
