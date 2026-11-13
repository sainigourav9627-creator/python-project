students = (
    ("Amit", 80),
    ("Sunil", 90),
    ("Anil", 35),
    ("Vipin", 60)
)
total = 0
highest = 0
topper = ""
lowest = 100
lowest_student = ""

for name,marks in students:
  print(name,marks)
  
  total = total+ marks
print("\nTotal = ", total)

average = total/(len(students))
print("Average = ", average)

for name,marks in students:
  if marks > highest:
    highest = marks
    topper = name
print("\nHighest = ",highest)
print("Topper = ", topper)

for name,marks in students:
  if marks < lowest:
    lowest = marks
    lowest_student = name
print("\nLowest = ",lowest)
print("Lowest_student = ", lowest_student)

for name,marks in students:
  if marks >= 40:
    print(name, "- Pass")
  else:
    print(name, "- Fail")

search = input("Enter student name: ")
found = False

for name, marks in students:
    if name.lower() == search.lower():
        found = True
        print("Student:", name)
        print("Marks:", marks)

        if marks >= 40:
            print("Result: Pass")
        else:
            print("Result: Fail")

if not found:
    print("Student Not Found")

topper_students = []
for name,marks in students:
  if marks >= 80:
    topper_students.append(name)
print(topper_students)

result = {}

for name, marks in students:
    result[name] = marks

print(sorted(result.items(), key=lambda item: item[1]))

result = {}

for name, marks in students:
    result[name] = marks

print(sorted(result.items(), key=lambda item: item[1],reverse=True))

for name, marks in students:
    if marks >= 90:
        grade = "A"
    elif marks >= 80:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 40:
        grade = "D"
    else:
        grade = "Fail"

    print(name, "-", marks, "-", grade)

pass_count = 0
fail_count = 0

for name, marks in students:
  if marks >= 40:
    pass_count = pass_count + 1
  else:
    fail_count = fail_count + 1
print("Pass Students", pass_count)
print("Fail Students", fail_count)

pass_count = 0

for name, marks in students:
    if marks >= 40:
        pass_count = pass_count + 1

total_students = len(students)
percentage = (pass_count / total_students) * 100

print("Pass Students =", pass_count)
print("Total Students =", total_students)
print("Pass Percentage =", percentage)

search = input("Enter name: ")
found = False

for name,marks in students:
  if name.lower() == search.lower():
    found = True
    print("Marks:", marks)
if not found:
  print("student not found")

names = []
for name,marks in students:
    names.append(name)
print(names)

marks_list = []
for name,marks in students:
    marks_list.append(marks)
print(marks_list)



  
    



  
    

