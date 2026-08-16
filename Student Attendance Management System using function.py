print("------- Student Attendance Management System -----")

def attendance():
   
    student = input("\nEnter student name       : ")
    attended = int(input("Enter attended classes   : "))
    total = int(input("Enter total classes      : "))

    print("\nStudent = ", student)
   
    
    percentage = (attended/total) * 100
    print("Attendance = ",  percentage)
    
    if percentage >= 75:
        status = "Eligible"
        
    else :
        status = " Not Eligible"
    
    return percentage , status

percentage , status = attendance()

print("status = " , status)

