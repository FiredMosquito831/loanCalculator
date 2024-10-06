import math
annuity_payment = float(input("Enter the annuity payment: "))
number_periods = int(input("Enter the number of periods: "))
loan_interest = float(input("Enter loan interest: "))
n = number_periods
i = loan_interest / (12 * 100)
A = annuity_payment
loan_principal = A / ((i * (math.pow((1 + i), n))) / (math.pow((1 + i), n) - 1))
print("Your loan principal = {}!".format(round(loan_principal)))
