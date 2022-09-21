print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
ch=int(input("Enter your choice "))
result=0
if( ch==1)or( ch==2 )or(ch==3 )or( ch==4):
    a=int(input("Enter a value for a : "))
    b=int(input("Enter a value for b : "))
    if(ch==1):
        print("Result = ",a+b)
    elif(ch==2):
        print("Result = ",a-b)
    elif(ch==3):
        print("Result = ",a*b)
    elif(ch==4):
        print("Result = ",a/b)
else:
    print("Invalid Input")

