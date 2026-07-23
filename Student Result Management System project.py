print("=======student management system========")
print("1.Pass/Fail")
print("2.Scholarship")
print("3.Voting Eligibility")
print("4.Grade")
print("5.Exit")
choice=int(input("enter the choice:"))

if choice == 1:
   marks=int(input("enter the marks:"))
   if marks>=33:
     print("pass")
   else:
     print("fail")

elif choice == 2:
   marks=int(input("enter the marks:"))
   sports = int(input("Enter sports (1/0): "))
   if marks >= 90 or sports == 1:
     print("scholarship")
   else:
     print("no scholarship")

elif choice == 3:
    age=int(input("Enter age: "))
    if age >= 18:
        print("Eligible")
    else:
        print("Not Eligible")

elif choice == 4:
    marks = int(input("enter the marks:"))
    if marks>=90 and marks<=100:
      print("A")
    elif marks>=75 and marks<=89:
     print("B")
    elif marks>=60 and marks<=74:
     print("c")
    elif marks>=33 and marks<=59:
     print("D")
    else:
       print("exit")
