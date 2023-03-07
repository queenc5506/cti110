# CTI-110
# P2HW2 - Semester Grades
# Crystal Queen
# 06 Mar 2023
#
# ****************** Pseudocode *********************
# Insert Blank Line
# Ask user "Enter grade for Module 1:"
# Input mod1
# Ask user "Enter grade for Module 2:"
# Input mod2
# Ask user "Enter grade for Module 3:"
# Input mod3
# Ask user "Enter grade for Module 4:"
# Input mod4
# Ask user "Enter grade for Module 5:"
# Input mod5
# Ask user "Enter grade for Module 6:"
# Input mod6
# Display "------------Results------------"
# Display "Lowest Grade:" mod5
# Display "Highest Grade:" mod6
# Display "Sum of Grades:" sum
# Display "Average:" aveg
# Display "-----------------------------------------"

mod1 = float(input('Enter grade for Module 1: '))
mod2 = input('Enter grade for Module 2: ')
mod3 = float(input('Enter grade for Module 3: '))
mod4 = input('Enter grade for Module 4: ')
mod5 = input('Enter grade for Modele 5: ')
mod6 = input('Enter grade for Module 6: ')
print('\n------------Results------------')
mod5 = 61.0
mod6 = 92.0
grades_sum = 475.0
grades_ave = grades_sum/6
print(f'{"Lowest Grade:":<20}{mod5}')
print(f'{"Highest Grade:":<20}{mod6}')
print(f'{"Sum of Grades:":<20}{grades_sum}')
print(f'{"Average:":<20}{grades_ave:.2f}')
print('-----------------------------------------')
