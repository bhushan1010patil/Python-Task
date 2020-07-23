# Program for simple calculator
print("Program for simple calculator")

while True:
    print("\n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Divison \n 5.Floor Division \n 6.Exponent \n 7.Exit \n")
    choice = input("Enter the choice:")
    if choice == '1':
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        print(f"The addition of {num1} and {num2} is",num1 + num2)
    elif choice == '2':
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        print(f"The subtraction of {num1} and {num2} is", num1 - num2)
    elif choice == '3':
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        print(f"The multiplication of {num1} and {num2} is", num1 * num2)
    elif choice == '4':
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        print(f"The division of {num1} and {num2} is", num1 / num2)
    elif choice == '5':
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        print(f"The floor division of {num1} and {num2} is", num1 // num2)
    elif choice =='6':
        num1 = int(input("Enter first number:"))
        num2 = int(input("Enter second number:"))
        print(f"The exponent of {num1} and {num2} is", num1 ** num2)
    elif choice == '7':
        break
    else:
        print("Please enter a valid choice")

print("Loop is terminated")