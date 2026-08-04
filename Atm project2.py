Current_Balance=1000
print("============= ATM Project ====================")

print("\n1.Check Balance")
print("2.Deposit")
print("3.Withdraw")
print("4.Exit")

choice = int(input("\nEnter Your Choice: "))


if choice == 1:
    print("Current Balance =", Current_Balance)

elif choice == 2:
    amount = int(input("Enter Deposit Amount: "))
    Current_Balance = Current_Balance + amount
    print("Current Balance =", Current_Balance)

elif choice == 3:
    amount = int(input("Enter Withdraw Amount: "))

    if amount <= Current_Balance:
        Current_Balance = Current_Balance - amount
        print("Current Balance =", Current_Balance)
    else:
        print("Insufficient Balance")

elif choice == 4:
    print("Exit")

else:
    print("Invalid Choice")
