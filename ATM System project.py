print("\n------ATM System--------")
atm_pin = 1234
balance=10000 
entered_pin = int(input("Enter PIN: "))


if entered_pin==atm_pin:
   print("welcome")
   print("\n------ATM Menu--------")
   print("1. Check Balance")
   print("2. Deposit")
   print("3. withdraw")
   print("4. Exit")
   
   choice = int(input("Enter your choice:"))

   if choice==1:
     print("Current Balance:", balance)
  
   elif choice==2:
    deposit=int(input("enter depsoit:"))
    balance = balance + deposit
    print("Current Balance:", balance)
   
   elif choice==3:
    withdraw=int(input("enter the withdraw:"))
    if withdraw<= balance:
       balance = balance - withdraw
       print("Current Balance:", balance)
    else:
        print("Insufficient Balance")
        
   elif choice == 4:
    print("Thank You for Using ATM!Visit Again.")  
   else:
    print("Invalid Choice")

else:
  print("Invalid PIN")
