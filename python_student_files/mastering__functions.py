#===========================================================================
# In Class Assignment - Mastering Functions in Python
# DEV 108 - 34634
# Mario Rodriguez
# February 12, 2025
#===========================================================================

def calculate_gross_salary(hourly_rate, hours_worked=40, bonus=0):
    gross_salary = (hourly_rate*hours_worked) + bonus
    return gross_salary

def calculate_deductions(gross_salary, tax_rate=0.15, insurance=50):
    total_deductions = (gross_salary*tax_rate) + insurance
    return total_deductions

def calculate_net_salary(gross_salary, deductions):
    net_salary = gross_salary - deductions
    return net_salary

def main():

    hourly_rate = float(input('Please enter the hourly rate: '))
    hours_worked = int(input('Please enter the hours worked (default 40): '))
    bonus = int(input('Please enter bonus (default 0): '))

    gross_salary = calculate_gross_salary(hourly_rate, hours_worked, bonus)
    deductions = calculate_deductions(gross_salary)
    net_salary = calculate_net_salary(gross_salary, deductions)

    print('===== Payroll Summary =====')
    print(f'Gross Salary: ${gross_salary}')
    print(f'Total Deductions: ${deductions}')
    print(f'Net Salary: ${net_salary}')

if __name__ == '__main__':
    main()
