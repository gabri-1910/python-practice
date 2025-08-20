## This is a calculator app
def calculator():
    print("To close the calculator app, set the operator to 0 (zero)")
    x = 1
    while x == 1:
        a = float(input("Enter a number: "))
        operator = str(input("Enter an operator: "))
        b = float(input("Enter a number: "))
        if operator == "+":
            result = a + b
            print(result)
        elif operator == "-":
            result = a - b
            print(result)
        elif operator == "*":
            result = a * b
            print(result)
        elif operator == "/":
            result = a / b
            print(result)
        elif operator == "0":
            break
        else:
            print("Please, enter the right operator")
        

calculator()