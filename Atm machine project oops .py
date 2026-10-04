class ATM:
    def __init__(self, balance):
        self.__balance = balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        if amount > self.__balance:
            raise ValueError("Insufficient balance")

        self.__balance = self.__balance - amount
        print("Withdraw successful")

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        self.__balance = self.__balance + amount
        print("Deposit successful")

    def get_balance(self):
        return self.__balance


atm = ATM(5000)

pin = 1234

entered_pin = int(input("Enter PIN: "))

if entered_pin != pin:
    print("Wrong PIN")
    exit()
else:
    print("PIN verified")


while True:
    print("\n1. Withdraw")
    print("2. Deposit")
    print("3. Check Balance")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter numbers only")
        continue

    if choice == 1:
        try:
            amount = int(input("Enter withdraw amount: "))
            atm.withdraw(amount)
        except ValueError as e:
            print(e)

    elif choice == 2:
        deposit_amount = int(input("Enter deposit amount: "))

        try:
            atm.deposit(deposit_amount)
        except ValueError as e:
            print(e)

    elif choice == 3:
        print("Balance:", atm.get_balance())

    elif choice == 4:
        print("Thank you for using ATM")
        break

    else:
        print("Invalid choice")
