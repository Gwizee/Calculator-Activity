def addition(a , b) :
    return a + b
def subtraction(a , b) :
    return a - b 
def multiplication(a , b) :
    return a * b 
def divition(a , b) :
    return a / b 

print("Please select an operator")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplacition")
print("4.Divition")

operator = int(input("Enter an operator [1 / 2 / 3 / 4]: "))
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if operator == 1 :
    print("The addition is :",addition(num1,num2))
elif operator == 2 :
    print("The subtraction is :",subtraction(num1,num2))
elif operator == 3 :
    print("The multuplication is :",multiplication(num1,num2))
elif operator == 4 :
    print("The divition is :",divition(num1,num2))
else :
    print("EROR 404 !!!!!!!!!!!!!!!!!!!!!!!!!!!")