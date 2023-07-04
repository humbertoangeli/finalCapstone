# This program asks the user which calculation he wants to do
# if he choices 'bond':
# the program it will ask for the value of the house, rate and months and it will
# calculate the monthly value with the formula: (rate/100/12 * present)/(1 - (1 + rate/100/12)**(-months))

# if he choices 'investment'
# the program it will ask for the amount to be invested, the rate, the years and the mode of calculation (simple or compound)
# if he choices 'simple' calculation:
# the program it will calculate the amount in the final period with the formula: present * (1 + rate/100 * years)
# if he choices 'compound' calculation:
# the program it will calculate the amount in the final period with the formula: present * math.pow((1 + rate/100), years)
import math
print("Which calculation do you want to do?")
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")
choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

if choice.lower() == "bond":
    present = int(input("Type the present value of the house: "))
    rate = int(input("Type the interest rate: "))
    months = int(input("The number of months they plan to take to repay the bond: "))
    repayment = (rate/100/12 * present)/(1 - (1 + rate/100/12)**(-months))
    print("You have to repay each month the value " + str(repayment) + " for " + str(months) + " months.")

elif choice.lower() == "investment":
    present = int(input("Type the amount of money you are depositing: "))
    rate = int(input("Type the interest rate (per year): "))
    years = int(input("Type the number of years are you planning to invest: "))
    mode = input("Type of interest (simple or compound): ")

    if mode.lower() == "simple":
        amount = present * (1 + rate/100 * years)
        print("your amount in the end of " + str(years) + " years, simple calculation it will be " + str(amount))
    elif mode.lower() == "compound":
        amount = present * math.pow((1 + rate/100), years)
        print("your amount in the end of " + str(years) + " years, compound calculation it will be " + str(amount))
    else:
        print("Sorry, you didn't type a valid option (simple or compound).")

else:
    print("Sorry, you didn't type a valid option (bond or investment).")
