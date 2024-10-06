n = 12
while n != 0:
    s = n / 12
    n = n - 1
    print(s)

import math
counts = 0
choice = input('''What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal: ''')
if choice == "n":
    loan_principal = int(input("Enter loan principal: "))
    monthly_payment = int(input("Enter monthly payment: "))
    loan_interest = float(input("Enter loan interest: "))
    i = loan_interest / (12 * 100)
    n = math.log(monthly_payment / (monthly_payment - i * loan_principal), 1 + i)

    counts = 0
    n = round(n, 2)
    n2 = round(n, 2)
    if isinstance(n2, float) and n > 12:
        while int(n2) % 10 != 0:  # while that sees how many decimals a number has
            n2 = n2 * 10          # depending on that we will know if we do months
            counts += 1
        counts = counts - 1
        if counts == 2:
            year = round(n)
            months = round((round(n, 1) - year) * 10 + 1)
            print("It will take {} years and {} months to repay this loan!".format(year, months))
        elif counts == 1:
            year = round(n)
            months = round((round(n, 1) - year) * 10)
            print("It will take {} years and {} months to repay this loan!".format(year, months))
        else:
            year = round(n)
            print("It will take {} years to repay this loan!".format(year))
    elif n == 12 or n == 12.0:
            year = n // 12
            print("It will take {} year to repay this loan!".format(round(year)))
    elif isinstance(n2, float) and n < 12:
        while int(n2) % 10 != 0:  # while that sees how many decimals a number has
            n2 = n2 * 10          # depending on that we will know if we do months
            counts += 1
        counts = counts - 1
        if counts == 2:
            year = round(n)
            months = round((round(n, 1) - year) * 10 + 1)
            print("It will take {} months to repay this loan!".format(months))
        elif counts == 1:
            year = round(n)
            months = round((round(n, 1) - year) * 10)
            print("It will take {} months to repay this loan!".format(months))



#What do you want to calculate?
#type "n" for number of monthly payments,
#type "a" for annuity monthly payment amount,
#type "p" for loan principal: > n
#Enter loan principal: > 500000
#Enter monthly payment: > 23000
#Enter loan interest: > 7.8
#It will take 24 years and -4 months to repay this loan!
