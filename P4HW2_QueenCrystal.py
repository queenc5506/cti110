# CTI-110
# P4HW2 - Salary Calculator
# Crystal Queen
# 19 Apr 2023
#
# ****************** Pseudocode *********************
# Ask user "Enter employee's name or "Done" to terminate:"
# Input emp
# Ask user "How many hours did" emp "work?"
# Input work_hours
# Ask user "What is" emp "'s pay rate?"
# Input pay_rate
# Display "Employee name:" emp
# Display "Hours Worked", "Pay Rate", "OverTime", "OverTime Pay", "RegHour Pay", "Gross Pay"
# Display "----------------------------------------------------------------------------"
# Display "work_hours, pay_rate, over_time, ot_pay, reg_pay, gross_pay"
# Ask user "Enter employee's name or "Done" to terminate:"
# Input emp
# Ask user "How many hours did" emp "work?"
# Input work_hours
# Ask user "What is" emp "'s pay rate?"
# Input pay_rate
# Display "Employee name:" emp
# Display "Hours Worked", "Pay Rate", "OverTime", "OverTime Pay", "RegHour Pay", "Gross Pay"
# Display "----------------------------------------------------------------------------"
# Display "work_hours, pay_rate, over_time, ot_pay, reg_pay, gross_pay"
# Ask user "Enter employee's name or "Done" to terminate:"
# Input "Done"
# Display "Total number of employees entered:" total_emp
# Display "Total amount paid for overtime:" total_ot
# Display "Total amount paid for regular hours:" total_reg
# Display "Total amount paid in gross:" total_gross

emp = input('Enter employee\'s name or "Done" to terminate: ')
total_emp = 0
total_ot = 0
total_reg = 0
total_gross = 0
while emp != 'Done':
    work_hours = float(input('How many hours did ' + emp + ' work? '))
    pay_rate = float(input('What is ' + emp + '\'s pay rate? '))
    over_time = work_hours - 40
    total_emp = total_emp + 1
    if over_time < 0:
        over_time = 0
    ot_pay = over_time * (pay_rate*1.5)
    total_ot = total_ot + ot_pay
    reg_hours = work_hours - over_time
    reg_pay = reg_hours * pay_rate
    total_reg = total_reg + reg_pay
    gross_pay = ot_pay + reg_pay
    total_gross = total_gross + gross_pay
    print(f'\n{"Employee name:":<17}', emp)
    print(f'\n{"Hours Worked":<15}{"Pay Rate":<12}{"OverTime":<12}{"OverTime Pay":<17}{"RegHour Pay":<16}{"Gross Pay":<12}')
    print('--------------------------------------------------------------------------------')
    print(f'{work_hours:<15}{pay_rate:<12.2f}{over_time:<12.1f}{ot_pay:<17.2f}${reg_pay:<16.2f}${gross_pay:<14.2f}')
    print('\n')
    emp = input('Enter employee\'s name or "Done" to terminate: ')
    
print('Total number of employees entered:', total_emp)
print('Total amount paid for overtime: ''$' + str(total_ot))
print(f'Total amount paid for regular hours: ${total_reg:.2f}')
print('Total amount paid in gross: ''$' + str(total_gross))

