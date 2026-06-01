num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
 
operation=input("Choose +,-,*,/,**,%,//,sqrt,%of,abs: ")
 
if operation=="+":
     result=num1+num2
elif operation=="-":
     result=num1-num2
elif operation=="*":
     result=num1*num2
elif operation=="/":
     result=num1/num2
elif operation=="**":
     result=num1**num2
elif operation=="%":
     result=num1%num2
elif operation=="//":
     result=num1//num2
elif operation=="sqrt":
     print("Square root of first number:", math.sqrt(num1))
     print("Square root of second number:", math.sqrt(num2))
     result="Square root Calculated"
elif operation=="%of":
     result=num1*num2/100
elif operation=="abs":
     result=abs(num1)
else:
     print("invalid operation")
