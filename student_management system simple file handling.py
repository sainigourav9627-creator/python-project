while True:

    print()
    print("===== STUDENT MANAGEMENT =====")

    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("0. Exit")

    choice = input("Enter choice: ")


    # 1. ADD

    if choice == "1":

        id = input("Enter ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        course = input("Enter Course: ")

        with open("student.txt", "a") as file:

            file.write(id + "," + name + "," + age + "," + course + "\n")

        print("Student Added")


    # 2. VIEW

    elif choice == "2":

        with open("student.txt", "r") as file:

            data = file.readlines()

        for line in data:

            print(line.strip())


    # 3. SEARCH

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


    # 4. UPDATE

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


    # 5. DELETE

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


    # EXIT

    elif choice == "0":

        print("Program Closed")

        break


    else:

        print("Wrong Choice")
