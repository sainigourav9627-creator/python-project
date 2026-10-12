
marks = [65, 80, 45, 90, 55]

while True:
    print("\n===== Student Marks Management System =====")
    print("1. View Marks")
    print("2. Add Marks")
    print("3. Remove Marks")
    print("4. Total and Average")
    print("5. Highest and Lowest")
    print("6. Sort Marks")
    print("7. Search Marks")
    print("8. Exit")

    try:
        choice = int(input("Enter your choice (1-8): "))
    except ValueError:
        print("Please enter a number from 1 to 8.")
        continue

    if choice < 1 or choice > 8:
        print("Invalid choice! Enter 1 to 8.")
        continue

    if choice == 1:
        if marks:
            print("Student Marks:", marks)
        else:
            print("No marks available.")

    elif choice == 2:
        try:
            new_mark = int(input("Enter new marks (0-100): "))

            if 0 <= new_mark <= 100:
                marks.append(new_mark)
                print("Marks added successfully.")
            else:
                print("Marks must be between 0 and 100.")

        except ValueError:
            print("Please enter numbers only.")

    elif choice == 3:
        try:
            remove_mark = int(input("Enter marks to remove: "))
            marks.remove(remove_mark)
            print("Marks removed successfully.")
        except ValueError:
            print("Invalid input or marks not found.")

        print("Current Marks:", marks)

    elif choice == 4:
        if marks:
            total = sum(marks)
            average = total / len(marks)

            print("Total Marks:", total)
            print("Average Marks:", round(average, 2))
        else:
            print("No marks available.")

    elif choice == 5:
        if marks:
            print("Highest Marks:", max(marks))
            print("Lowest Marks:", min(marks))
        else:
            print("No marks available.")

    elif choice == 6:
        marks.sort()
        print("Sorted Marks:", marks)

    elif choice == 7:
        try:
            search_mark = int(input("Enter marks to search: "))

            if search_mark in marks:
                print("Marks found.")
            else:
                print("Marks not found.")

        except ValueError:
            print("Please enter numbers only.")

    elif choice == 8:
        print("Program closed.")
        break
