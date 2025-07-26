def main(operation, num1, num2):
    if operation == "*":
        result = (num1 * num2)
        print("The result is:", result)
    elif operation == "/":
        result = (num1 / num2)
        print("The result is:", result)
    elif operation == "+":
        result = (num1 + num2)
        print("The result is:", result)
    elif operation == "-":
        result = (num1 - num2)
        print("The result is:", result)
    else:
        return "The code just broke"

print("This is a simple calculator:")
print("Below, you will choose two numbers and a operator:")

num1 = int(input("Choose a number: "))
operator = str(input("Between the following operators: *, /, +, - choose an operator: "))
num2 = int(input("Choose a number: "))

main(operator, num1, num2)