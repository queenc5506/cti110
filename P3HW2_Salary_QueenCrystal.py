# CTI-110
# P3HW2 - Salary
# Crystal Queen
# 27 Mar 2023
#
# ****************** Pseudocode *********************
# Ask user "Enter employee's name:"
# Input emp
# Ask user "Enter number of hours worked:"
# Input work_hours
# Ask user "Enter employee's pay rate:"
# Input pay_rate
# Display "----------------------------------"
# Display "Employee name:" emp
# Display "Hours Worked", "Pay Rate", "OverTime", "OverTime Pay", "RegHour Pay", "Gross Pay"
# Display "----------------------------------------------------------------------------"
# Display "work_hours, pay_rate, over_time, ot_pay, reg_pay, gross_pay"

emp = input("Enter employee's name: ")
work_hours = float(input('Enter number of hours worked: '))
pay_rate = float(input("Enter employee's pay rate: "))
over_time = work_hours - 40
ot_pay = over_time * (pay_rate*1.5)
reg_hours = work_hours - over_time
reg_pay = reg_hours * pay_rate
gross_pay = ot_pay + reg_pay

print('--------------------------------------')
print(f'{"Employee name:":<17}', emp)
print(f'\n{"Hours Worked":<15}{"Pay Rate":<12}{"OverTime":<12}{"OverTime Pay":<17}{"RegHour Pay":<16}{"Gross Pay":<12}')
print('--------------------------------------------------------------------------------')
print(f'{work_hours:<15}{pay_rate:<12}{over_time:<12}{ot_pay:<17}${reg_pay:<16.2f}${gross_pay:<14.2f}')
