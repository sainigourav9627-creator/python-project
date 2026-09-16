balance = 5000
print("Current Balance :", balance)

try:
    deposit_amount = int(input("enter the deposit amount : "))

    if deposit_amount <= 0:
        raise ValueError("galat amount")

    balance = balance + deposit_amount
    print("New balance :", balance)

    
  withdraw_amount = int(input("enter the withdraw amount : "))

    if withdraw_amount <= 0:
        raise ValueError("galat amount")

    if withdraw_amount <= balance:
        balance = balance - withdraw_amount
        print("Current balance :", balance)
    else:
      raise ValueError("Insufficient balance")


except ValueError as e:
    print(e)
else:
  print("Transaction successful")
finally:
    print("Thank you for using ATM")
