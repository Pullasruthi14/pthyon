n1=int(input("Enter numbers:"))
n2=int(input(""))
if(n1<=0 or n2<=0):
    print("Enter a positive number.")
elif(n1%n2==0):
    print(n2)
elif(n2%n1==0):
    print(n1)
else:
    print("Invalid input.")
