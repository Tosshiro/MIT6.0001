# Problem Set 1a, ps1a.py
# @author Jw

while True:
    try:
        annual_salary = float(input("Enter your annual salary: "))
        portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
        total_cost = float(input("Enter the cost of your dream house: "))
        break

    except ValueError:
        print("Not valid number")

current_savings = 0
down_payment = 0.25 * total_cost
monthly_salary = annual_salary/12
number_of_months = 0

while current_savings < down_payment:
    current_savings += (monthly_salary * portion_saved) + \
        (current_savings * 0.04/12)
    number_of_months += 1


print("Number of months needed: " + str(number_of_months))
