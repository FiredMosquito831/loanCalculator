import math
loan_principal = int(input("Enter loan principal: "))
monthly_payment = int(input("Enter monthly payment: "))
loan_interest = float(input("Enter loan interest: "))
i = loan_interest / (12 * 100)
n = math.log(monthly_payment / (monthly_payment - i * loan_principal), 1 + i)
years = n / 12
months = (round(years) - years) * 100
months = abs(round(months))
years = abs(round(years))
count = 0
n2 = months
while n2 != 0:
    n2 //= 10
    count += 1
if count == 2:
    months = round(months / 10 + 1)
    print("It will take {} years and {} months to repay this loan!".format(years, months))
elif count == 1:
    months = round(months / 10)
    if months != 0:
        print("It will take {} years and {} months to repay this loan!".format(years, months))
    elif months == 0:
        print("It will take {} years to repay this loan!".format(years))
elif count == 0:
    months = 0
    months = round(months)
    if years > 1:
        print("It will take {} years to repay this loan!".format(years))
    elif years == 1:
        print("It will take {} year to repay this loan!".format(years))
if n == 12 or n == 12.0 or n == 12.00:
    print("It will take 1 year to repay this loan!")


# 500000   23000   7.8
