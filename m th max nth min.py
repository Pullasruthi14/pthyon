a=int(input("enter the number:"))
b=[]
for i in range(0,a):
    c=int(input("enter the element:"))
    b.append(c)
print("list of element:",b)
m=int(input("M="))
n=int(input("N="))
if(m<=0 or m>a or n<=0 or n>a):
    print("invalid input")
else:
    b.sort()
    for i in range(0,a):
        if(n-1==i):
            d=b[i]
    b.reverse()
    for i in range(0,a):
        if(m-1==i):
            e=b[i]
    print("Sum=",d+e)
    print("Difference=",e-d)
