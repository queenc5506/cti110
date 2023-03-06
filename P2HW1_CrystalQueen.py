# Program calculates the cost of travel
# 04 Mar 2023
# CTI-110 P2HW1 - Travel
# Crystal Queen
#
# ****************** Pseudocode *********************
# Insert Blank Line
# Display "This program calculates and displays travel expenses"
# Ask user "Enter Budget:"
# Input budget
# Ask user "Enter your travel destination:"
# Input destination
# Ask user "How much do you think you will spend on gas?"
# Input gas
# Ask user "Approximately, how much will you need for accomodation/hotel?"
# Input accomodation
# Ask user "Last, how much do you need for food?"
# Input food
# Display "------------Travel Expenses------------"
# Display "Location:" destination
# Display "Initial Budget:" $budget
# Display "Fuel:" $gas
# Display "Accomodation:" $accomodation
# Display "Food:" $food
# Display "-----------------------------------------"
# Display "Remaining Balance:" $balance

print('This program calculates and displays travel expenses')
budget = float(input('\nEnter Budget: '))
destination = input('\nEnter your travel destination: ')
gas = float(input('\nHow much do you think you will spend on gas? '))
accomodation = float(input('\nApproximately, how much will you need for accomodation/hotel? '))
food = float(input('\nLast, how much do you need for food? '))
print('\n------------Travel Expenses------------')
expenses = gas + accomodation + food
balance = budget - expenses
print(f'{"Location:":<20}{destination}')
print(f'{"Initial Budget:":<20}${budget}')
print(f'{"Fuel:":<20}${gas}')
print(f'{"Accomodation:":<20}${accomodation}')
print(f'{"Food:":<20}${food}')
print('-----------------------------------------')
print(f'\n{"Remaining Balance:":<20}${balance}')

