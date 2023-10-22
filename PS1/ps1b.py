# Problem Set 1a, ps1a.py
# @author Jw

while True:
    try:
        annual_salary = float(input("Enter your annual salary: "))
        portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
        total_cost = float(input("Enter the cost of your dream house: "))
        semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))
        break

    except ValueError:
        print("Not valid number")

current_savings = 0
down_payment = 0.25 * total_cost
monthly_salary = annual_salary/12
number_of_months = 0

while current_savings < down_payment:
    number_of_months += 1
    monthly_salary = annual_salary / 12
    current_savings += (monthly_salary * portion_saved) + \
        (current_savings * (0.04/12))

    #  increase in annual salary every 6 months
    if number_of_months % 6 == 0:
        annual_salary += (annual_salary * semi_annual_raise)

print("Number of months needed: " + str(number_of_months))
