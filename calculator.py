def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y

def main():
    print("Select an Operation\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
    while True:
        question = int(input(">> "))
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))
        try:
            if question == 1:
                print("{0} + {1} = {2}".format(num1, num2, addition(num1, num2)))
            elif question == 2:
                print("{0} - {1} = {2}".format(num1, num2, subtraction(num1, num2)))
            elif question == 3:
                print("{0} x {1} = {2}".format(num1, num2, multiplication(num1, num2)))
            elif question == 4:
                print("{0} ÷ {1} = {2}".format(num1, num2, division(num1, num2)))
            else:
                print("Enter a valid input")
        except TypeError:
            print("Enter a vaild input")

main()