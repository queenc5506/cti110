# Program calculates the cost of travel
# 20 Feb 2023
# CTI-110 P1HW2 - Travel Expense
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
# Display "Initial Budget:" budget
# Display "Fuel:" gas
# Display "Accomodation:" accomodation
# Display "Food:" food
# Display "Remaining Balance:" balance

print('This program calculates and displays travel expenses')
budget = float(input('\nEnter Budget: '))
destination = input('\nEnter your travel destination: ')
gas = float(input('\nHow much do you think you will spend on gas? '))
accomodation = float(input('\nApproximately, how much will you need for accomodation/hotel? '))
food = float(input('\nLast, how much do you need for food? '))
print('\n------------Travel Expenses------------')
expenses = gas + accomodation + food
balance = budget - expenses
print('Location:', destination)
print('Initial Budget:', budget)
print('\nFuel:', gas)
print('Accomodation:', accomodation)
print('Food:', food)
print('\nRemaining Balance:', balance)
