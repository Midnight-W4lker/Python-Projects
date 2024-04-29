import math
#CREATING A SIMPLE SCIENTIFIC CALCULATOR with Python:
#1. Add
#2. Subtract
#3. Multiply
#4. Divide
#5. Square Root
#6. Power

print("Select an Opertion")
print("1. ADDITION")
print("2. SUBTRACTION")
print("3. MULTIPLICATION")
print("4. DIVISION")
print("5. SQUARE ROOT")
print("6. POWER")

operation = input("Select an OPERATION (1-6)")
#Code for ADDITION
if operation == "1":
    num1 = input("Enter 1st Number")
    num2 = input("Enter 2nd Number")
    print("          The SUM is " + str(int(num1) + int(num2)))
    
#Code for SUBTRACTION
elif operation == "2":
    num1 = input("Enter 1st Number")
    num2 = input("Enter 2nd Number")
    print("          The DIFFERENCE is " + str(int(num1) - int(num2)))
    
#Code for MULTIPLICATION
elif operation == "3":
    num1 = input("Enter 1st Number")
    num2 = input("Enter 2nd Number")
    print("          The PRODUCT is " + str(int(num1) * int(num2)))
    
#Code for DIVISION
elif operation == "4":
    num1 = input("Enter 1st Number")
    num2 = input("Enter 2nd Number")
    print("          The RESULT is " + str(int(num1) / int(num2)))
    
#Code for SQUARE ROOT    
elif operation == "5":
    num = int(input("Enter Number"))
    print("          The SQUARE ROOT is %f "  %(math.sqrt(num)))

#Code for POWER    
elif operation == "6":
    num1 = int(input("Enter Number"))
    num2 = int(input("Enter Power"))
    print("          The RESULT is %d "  %(math.pow(num1, num2)))
            
else:
    print("Invalid Operation")  
