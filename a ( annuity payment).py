import math
loan_principal = int(input("Enter loan principal: "))
number_periods = int(input("Enter the number of periods: "))
loan_interest = float(input("Enter loan interest: "))
i = loan_interest / (12 * 100)
n = number_periods
A = loan_principal * ((i * math.pow((1 + i), n)) / (math.pow((1 + i), n) - 1))
if isinstance(A, float):
    A = A + 1
    print(round(A))
else:
    print(round(A))
