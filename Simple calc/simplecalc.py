print("what u want to perform:\n1.Addition\n2.Subtraction\n3.multiplication\n4.division")
take=int(input())

num1=float(input("enter no.1 :"))
num2=float(input("enter no.2 :"))
if take==1:
    result=num1+num2

if take==2:
     result=num1-num2

if take==3:
    result=num1*num2

if take==4:
    result=num1/num2 

print(result)
