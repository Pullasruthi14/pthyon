total_user=int(input("enter the no of total users="))
staff_user=int(input("enter the no of staff user="))
if(total_user<=0 & staff_user<=0):
    print("enter a valid input")
else:
    t_user=staff_user/3
    student_user=total_user-staff_user-t_user
    print(student_user)
