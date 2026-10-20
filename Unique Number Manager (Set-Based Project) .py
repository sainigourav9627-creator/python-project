print("------- Unique Number Manager ----------")


number = set()
number2 = {30, 40}

while True:
  print("\n1. Add number")
  print("2. View numbers")
  print("3. Count unique numbers ")
  print("4. Union")
  print("5. Intersection")
  print("6. Exit")

  choice = input("Enter your choice: ")


  if choice == "2":
    print(number)

  elif choice == "3":
    print(len(number))

  elif choice == "4":
    print(number.union(number2))

  elif choice == "5":
    print(number.intersection(number2))

  elif choice == "1":
    try:
        new_number = int(input("Enter number: "))
        number.add(new_number)
        print(number)
    except ValueError:
        print("Please enter a valid number!")
    

  elif choice == "6":
    print("Exiting program...")
    break
 
  else:
    print("Invalid choice! Try again.")
