num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
 
operation=input("Choose +,-,*,/,**,%,//,sqrt: ")
 
if operation=="+":
     print(num1+num2)
elif operation=="-":
     print(num1-num2)
elif operation=="*":
     print(num1*num2)
elif operation=="/":
     print(num1/num2)
elif operation=="**":
     print(num1**num2)
elif operation=="%":
     print(num1%num2)
elif operation=="//":
     print(num1//num2)
elif operation=="sqrt":
     print("Square root of first number:", math.sqrt(num1))
     print("Square root of second number:", math.sqrt(num2))
else:
     print("invalid operation")
