# This loop is needed to use the code again.
while True:
    # Loop checks for valid user input.
    while True:
        try:
            first_number = float(input("\nPlease enter the first number: "))
            second_number = float(input("Please enter the second number: "))
            # The loop breaks when the user enters two numbers.
            break
        # This block is triggered if the user enters something other than numbers.
        except ValueError:
            print("\nIt's not a number. Please try again!")

    multiplication = ['*']
    division = ['/']
    addition = ['+']
    subtraction = ['-']

    # Loop checks for valid user input.     
    while True:
        # Requesting the type of operation.
        operation = str(input("\nEnter the '*', '/', '+' or '-' operation you want to do with the numbers: "))
        if operation not in multiplication and operation not in division and operation not in addition and operation not in subtraction:
            print("\nIt's not a '*', '/', '+' or '-'. Try againe!")  
            continue
        else:
            # The loop breaks when the user enters '*', '/', '+' or '-'.
            break
        
    # Equation calculation.
    if operation == "*":
        equation_result = first_number * second_number
        print(f"\n{first_number} {operation} {second_number} = {equation_result} \n")
    elif operation == "/":
        equation_result = first_number / second_number
        print(f"\n{first_number} {operation} {second_number} = {equation_result} \n")
    elif operation == "+":
        equation_result = first_number + second_number
        print(f"\n{first_number} {operation} {second_number} = {equation_result} \n")
    else:
        operation == "-"
        equation_result = first_number - second_number
        print(f"\n{first_number} {operation} {second_number} = {equation_result} \n")

    file_name = str(input("Enter the file name you want to use to store the equations: "))

    # Writing to a file the equations entered by the user.
    try:
        file = open(f'{file_name}.txt', 'a+')
        # Format to a string to write the equation to a file.
        file.write(f"{first_number} {operation} {second_number} = {equation_result} \n")
        # Move the pointer to the beginning of the file to read the file.
        file.seek(0)
    except FileNotFoundError:
        print("\nThe file that you are trying to open does not exist.")
        # Closing a file.
        file.close()

    yes = ['yes']
    no = ['no']

    # Loop checks for valid user input.
    while True:
        # Ask the user if they want to do another equation.
        next_equation = str(input("\nYou want to run another equation or exit the program? Enter 'yes' or 'no': "))
        next_equation = next_equation.lower()
        if next_equation not in yes and next_equation not in no:
            print("\nYou have not chosen anything. Try againe!")  
            continue
        else:
            break 
    # The while loop starts again to do one more equation.
    if next_equation == "yes":
        continue
    # The loop is break.
    else: 
        next_equation == "no"
        break

# Printing equations from a file.
print(file.read())
# Closing a file.
file.close()