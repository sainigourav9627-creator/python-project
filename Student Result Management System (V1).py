print("\n==============  Student Result Management System  ==========")
student_name=input("\nEnter the Student Name:")
roll_number=int(input("Enter the Roll Number:"))
hindi=int(input("\nEnter the Hindi     :"))
english=int(input("Enter the English   :"))
math=int(input("Enter the Math      :"))
science=int(input("Enter the Science   :"))
computer=int(input("Enter the Computer  :"))

total=hindi+english+math+science+computer
print("\nTotal=",total)

#percentage = total / 5
percentage = (total / 500) * 100
print("Percentage=",percentage)

if percentage >= 90:
   print("Grade: A Grade")
elif percentage >= 75:
    print("Grade: B Grade")
elif percentage >= 60:
    print("Grade: C Grade")
elif percentage >= 40:
    print("Grade: D Grade")
else:
   print("Grade: Fail")
   
print("\n============== Student Result ==============")

print("Student Name :", student_name)
print("Roll Number  :", roll_number)
print("Total        :", total)
print("Percentage   :", percentage)
