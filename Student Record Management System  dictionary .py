print("----- Student Record Management System -----")

student = {
    101: {"name": "aman", "marks": 85}
}

while True:

    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter choice: ")

    # 1. Add Student
    if choice == "1":

        a = int(input("Enter student ID: "))
        b = input("Enter student name: ")
        c = int(input("Enter student marks: "))

        if a not in student:
            student[a] = {
                "name": b,
                "marks": c
            }
            print("Student Added Successfully")
        else:
            print("Student ID Already Exists")

    # 2. View Students
    elif choice == "2":

        if student:
            for student_id, details in student.items():
                print("\nID:", student_id)
                print("Name:", details["name"])
                print("Marks:", details["marks"])
        else:
            print("No Students Found")

    # 3. Search Student
    elif choice == "3":

        search_id = int(input("Enter ID: "))

        if search_id in student:
            details = student[search_id]
            print("Name:", details["name"])
            print("Marks:", details["marks"])
        else:
            print("Student Not Found")

    # 4. Update Student
    elif choice == "4":

        student_id = int(input("Enter ID: "))

        if student_id in student:

            details = student[student_id]

            new_name = input("Enter new name: ")
            details["name"] = new_name

            new_marks = int(input("Enter new marks: "))
            details["marks"] = new_marks

            print("Student Updated Successfully")

        else:
            print("Student Not Found")

    # 5. Delete Student
    elif choice == "5":

        student_id = int(input("Enter ID: "))

        if student_id in student:
            del student[student_id]
            print("Student Deleted Successfully")
        else:
            print("Student Not Found")

    # 6. Exit
    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
