# CTI-110
# P3HW1 - Semester Grades
# Crystal Queen
# 22 Mar 2023
#
# ****************** Pseudocode *********************
# Insert Blank Line
# Ask user "Enter grade for Module 1:"
# Input mod_1
# Ask user "Enter grade for Module 2:"
# Input mod_2
# Ask user "Enter grade for Module 3:"
# Input mod_3
# Ask user "Enter grade for Module 4:"
# Input mod_4
# Ask user "Enter grade for Module 5:"
# Input mod_5
# Ask user "Enter grade for Module 6:"
# Input mod_6
# Display "------------Results------------"
# Display "Lowest Grade:" min(grades)
# Display "Highest Grade:" max(grades)
# Display "Sum of Grades:" sum(grades)
# Display "Average:" Avg
# Display "-----------------------------------------"
# Display "Your grade is: B"


mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

print('\n------------Results------------')
print(f'{"Lowest Grade: ":<20}', min(grades))
print(f'{"Highest Grade: ":<20}', max(grades))
print(f'{"Sum of Grades: ":<20}', sum(grades))
Avg = sum(grades) / len(grades)
print(f'{"Average: ":<20}{Avg: .2f}')
print('-----------------------------------------')


if Avg >= 90:
    print('Your grade is: A')

elif Avg >= 80:
    print('Your grade is: B')

elif Avg >= 70:
    print('Your grade is: C')

elif Avg >= 60:
    print('Your grade is: D')

else:
    print('Your grade is: F')
