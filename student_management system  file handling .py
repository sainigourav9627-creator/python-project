import os
import json
import csv


while True:

    print()
    print("===== STUDENT MANAGEMENT =====")

    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. File Information")
    print("7. Create File")
    print("8. Save JSON")
    print("9. Read JSON")
    print("10. Save CSV")
    print("11. Read CSV")
    print("0. Exit")

    choice = input("Enter choice: ")


    # ADD

    if choice == "1":

        id = input("Enter ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        course = input("Enter Course: ")

        with open("student.txt", "a") as file:

            file.write(id + "," + name + "," + age + "," + course + "\n")

        print("Student Added")


    # VIEW

    elif choice == "2":

        with open("student.txt", "r") as file:

            data = file.readlines()

        for line in data:

            print(line.strip())


    # SEARCH

    elif choice == "3":

        id = input("Enter ID: ")

        with open("student.txt", "r") as file:

            data = file.readlines()

        for line in data:

            student = line.strip().split(",")

            if student[0] == id:

                print("ID:", student[0])
                print("Name:", student[1])
                print("Age:", student[2])
                print("Course:", student[3])

                break


    # UPDATE

    elif choice == "4":

        id = input("Enter ID: ")

        with open("student.txt", "r") as file:

            data = file.readlines()

        new = []

        for line in data:

            student = line.strip().split(",")

            if student[0] == id:

                name = input("New Name: ")
                age = input("New Age: ")
                course = input("New Course: ")

                line = id + "," + name + "," + age + "," + course + "\n"

            new.append(line)


        with open("student.txt", "w") as file:

            file.writelines(new)

        print("Student Updated")


    # DELETE

    elif choice == "5":

        id = input("Enter ID: ")

        with open("student.txt", "r") as file:

            data = file.readlines()

        new = []

        for line in data:

            student = line.strip().split(",")

            if student[0] != id:

                new.append(line)


        with open("student.txt", "w") as file:

            file.writelines(new)

        print("Student Deleted")


    # FILE INFORMATION

    elif choice == "6":

        if os.path.exists("student.txt"):

            print("File exists")
            print("File size:", os.path.getsize("student.txt"))

        else:

            print("File not found")


    # CREATE FILE

    elif choice == "7":

        try:

            with open("newfile.txt", "x") as file:

                file.write("New Student File")

            print("File Created")

        except FileExistsError:

            print("File already exists")


    # SAVE JSON

    elif choice == "8":

        with open("student.txt", "r") as file:

            data = file.readlines()

        students = []

        for line in data:

            student = line.strip().split(",")

            students.append({
                "id": student[0],
                "name": student[1],
                "age": student[2],
                "course": student[3]
            })


        with open("students.json", "w") as file:

            json.dump(students, file, indent=4)

        print("JSON Saved")


    # READ JSON

    elif choice == "9":

        with open("students.json", "r") as file:

            data = json.load(file)

        for student in data:

            print(student)


    # SAVE CSV

    elif choice == "10":

        with open("student.txt", "r") as file:

            data = file.readlines()


        with open("students.csv", "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow(["ID", "Name", "Age", "Course"])


            for line in data:

                student = line.strip().split(",")

                writer.writerow(student)

        print("CSV Saved")


    # READ CSV

    elif choice == "11":

        with open("students.csv", "r") as file:

            data = csv.reader(file)

            for row in data:

                print(row)


    # EXIT

    elif choice == "0":

        print("Program Closed")

        break


    else:

        print("Wrong Choice")
