# CTI-110
# P4HW1 - Score List
# Crystal Queen
# 12 April 2023
#
# ****************** Pseudocode *********************
# Ask user "How many scores do you want to enter?"
# Input scores
# Ask user "Enter score #1:"
# Input score1
# Ask user "Enter score #2:"
# Input score2
# Ask user "Enter score #3:"
# Input score3
# Display "INVALID Score entered!!!!"
# Display "Score should be between 0 and 100"
# Ask user "Enter score #3 again:"
# Input score3
# Ask user "Enter score #4:"
# Input score4
# Ask user "Enter score #5:"
# Input score5
# Display "--------------Results-----------"
# Display "Lowest Score  :" score4
# Display "Modified List :" score1, score2, score3, score5
# Dsiplay "Scores Average:" ave
# Display "Grade         : C"
# Display "-----------------------------------"

low = 100
scores = int(input('How many scores do you want to enter? '))
print('')
score_list = []
entries = 1
while entries < scores + 1:
    score1 = int(input('Enter score #' + str(entries) + ': '))
    while score1 < 0:
        print('\nINVALID Score entered!!!!')
        print('Score should be between 0 and 100')
        score1 = int(input('Enter score #' + str(entries) + ' again: '))
    while score1 > 100:
        print('\nINVALID Score entered!!!!')
        print('Score should be between 0 and 100')
        score1 = int(input('Enter score #' + str(entries) + ' again: '))
    
    score_list.append(float(score1))
    entries = entries + 1
    if low > score1:
        low = score1

score_list.remove(low)
low = float(low)
sum = sum(score_list)
ave = sum / (scores - 1)

print('\n--------------Results-----------')
print(f'{"Lowest Score":<14}: {low}')
print(f'{"Modified List":<14}: {score_list}')
print(f'{"Scores Average":<12}: {ave:.2f}')


if ave >= 90:
    print('Grade: A')
elif ave >= 80:
    print('Grade: B')
elif ave >= 70:
    print(f'{"Grade":<14}: C')
print('-----------------------------------')
