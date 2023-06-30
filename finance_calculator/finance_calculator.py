import math

# Ask user choice which calculation he wants to perform.
print('''investment - to calculate the amount of interest you'll earn on your investment \nbond \t   - to calculate the amount you'll have to pay on a home loan \n''')
calculation_type = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

# In case the user uses capital letters when entering data.
calculation_type = calculation_type.lower()

# Checking the correctness of user input.
if len(calculation_type) == 0:
    print("You haven't entered anything. Enter 'investment' or 'bond'.")
elif len(calculation_type) < 4:
    print("You have entered less than 4 characters. Please make sure that you have entered 'investment' or 'bond'")
elif len(calculation_type) > 10:
    print("You have entered more than 10 characters. Please make sure that you have only entered 'investment' or 'bond'")
else:
    print("Thank you for entering which calculation you want to perform.")

# If the user has entered an investment, we do this calculation.
if calculation_type == "investment":
    # Ask the user to enter the data necessary for the calculation.
    P = int(input("Enter the amount you wish to deposit: "))
    # The data entered by the user is divided by 100 to calculate the percentage.
    r = int(input("Enter the interest rate as a percentage. Only number e.g. 8: ")) / 100
    t = int(input("Enter number of years you want to invest: "))
    # Ask the user to select the simple or compound interest he wants to calculate.
    interest = input("\nEnter you want 'simple' or 'compound' interest: ")
    # In case the user uses capital letters when entering data.
    interest = interest.lower()
    # Simple interest calculation.
    if interest == "simple":
        A = P*(1 + r*t)
        # Print the sum by displaying 2 decimal places.
        print(f"The amount of simple interest you earn on your investment: {A:.2f} ")
    # Compound interest calculation.    
    elif interest == 'compound':
        A = P * math.pow((1+r),t)
        print(f"The amount of compond interest you earn on your investment: {A:.2f} ")
    else:
        print("Please make sure that you have only enterd 'simple' or 'compound' interest")
# If the user has entered an bond, we do this calculation.
elif calculation_type == "bond":
    # Ask the user to enter the data necessary for the calculation.
    P = int(input("Enter the present value of the house. e.g. 100000: "))
    # The data entered by the user is divided by 100 to calculate the percentage, and divide by 12 to convert it to a monthly rate.
    i = int(input("Enter the interest rate. Only number e.g. 7: ")) / 100 / 12
    n = int(input("Enter the number of months you plan to take to repay the bond. e.g. 120: "))
    repayment = (i * P)/(1 - (1 + i)**(-n))
    print(f"\nYou will have to repay each month: {repayment:.2f} ")
else:
    print("Please make sure that you have only entered 'investment' or 'bond'")