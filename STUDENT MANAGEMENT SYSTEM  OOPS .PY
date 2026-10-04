print("------------- STUDENT MANAGEMENT SYSTEM -------------")

students = []


class Student:
    def __init__(self, name, age, course, marks):
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks


while True:

    print("\n------------- MENU -------------")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    # 1. Add Student
    if choice == "1":

        name = input("Enter name: ")
        age = int(input("Enter age: "))
        course = input("Enter course: ")
        marks = int(input("Enter marks: "))

        student = Student(name, age, course, marks)

        students.append(student)

        print("Student added successfully")


    # 2. View Students
    elif choice == "2":

        if len(students) == 0:
            print("No students found")

        else:
            for student in students:
                print("\nName:", student.name)
                print("Age:", student.age)
                print("Course:", student.course)
                print("Marks:", student.marks)


    # 3. Search Student
    elif choice == "3":

        search = input("Enter student name to search: ")

        found = False

        for student in students:
            if student.name == search:

                print("\nName:", student.name)
                print("Age:", student.age)
                print("Course:", student.course)
                print("Marks:", student.marks)

                found = True

        if found == False:
            print("Student not found")


    # 4. Update Student
    elif choice == "4":

        update_name = input("Enter student name to update: ")

        found = False

        for student in students:
            if student.name == update_name:

                new_marks = int(input("Enter new marks: "))

                student.marks = new_marks

                print("Student updated successfully")

                found = True

        if found == False:
            print("Student not found")


    # 5. Delete Student
    elif choice == "5":

        delete_name = input("Enter student name to delete: ")

        found = False

        for student in students:
            if student.name == delete_name:

                students.remove(student)

                print("Student deleted successfully")

                found = True
                break

        if found == False:
            print("Student not found")


    # 6. Exit
    elif choice == "6":

        print("Thank you for using Student Management System")

        break


    # Wrong choice
    else:

        print("Invalid choice")
