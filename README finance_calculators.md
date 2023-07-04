# finance_calculators.md

## This program asks the user which calculation he wants to do
## if he choices 'bond':
## the program it will ask for the value of the house, rate and months and it will
## calculate the monthly value with the formula: (rate/100/12 * present)/(1 - (1 + rate/100/12)**(-months))

## if he choices 'investment'
## the program it will ask for the amount to be invested, the rate, the years and the mode of calculation (simple or compound)
## if he choices 'simple' calculation:
## the program it will calculate the amount in the final period with the formula: present * (1 + rate/100 * years)
## if he choices 'compound' calculation:
## the program it will calculate the amount in the final period with the formula: present * math.pow((1 + rate/100), years)

This program is an example of defensive programming with many manipulations of strings and numbers
and interations with the user
