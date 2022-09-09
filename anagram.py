def Anogram_check(string1, string2):
 if(sorted(string1)== sorted(string2)):
     print("Both strings form a Anogram.")
 else:
     print("Both strings do not form as a Anogram.")
string1=input("enter the 1st string")
string2=input("enter the 2nd string")
Anogram_check(string1, string2)
