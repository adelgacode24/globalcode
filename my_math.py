def calculate(operation, num1, num2):
    operation=operation.lower()

    if operation =="add":
        result= num1 +num2
    elif operation =="multiply":
        result = num1 * num2
    elif operation =="subtract":
            result = num1 - num2

    elif operation =="divide":
        if num1==0:
            print( "Zero is not divisible")
            exit()

        else:
            result=num1/num2

    print(f"result {result}")



num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
operation=input("Enter operation(add,subtract,multiply or dvide)")

calculate(operation, num1, num2)