def calculator():
    print("Welcome to the Calculator!")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Substraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    while True:
        choice = input("Enter number of operation (1/2/3/4): ")

        if choice in ('1', '2', '3', '4'):
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                summ = int(a) + int(b)
                diff = int(a) - int(b)
                multi = int(a) * int(b)
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue

            if choice == '1':
                print(f"Answer: {summ}")
            elif choice == '2':
                print(f"Answer: {diff}")
            elif choice == '3':
                print(f"Answer: {multi}")
            elif choice == '4':
                if (b == 0):
                    print("You cant divide by zero! Please change the numbers")
                    break
                else:
                     print(f"Answer: ", float(a / b))
        else:
            print("Invalid choice! Please enter a valid operation")


        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            print("Thank you for using the calculator. Goodbye!")
            break        

calculator()