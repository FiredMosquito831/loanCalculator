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
    print(n)
    years = n // 12
    print(years)
    months = (round(years) - years) * 100
    print(months, "luni inainte de schimbare")
    months = abs(round(months))
    print(months, "dupa schimbare")
    years = abs(round(years))
    count = 0
    n2 = months
    while n2 != 0:
        n2 //= 10
        count += 1
    if count == 2:
        months = round(months / 10 + 1)
        print("It will take {} years and {} months to repay this loan!".format(years, months))
        print("count == 2 ")
    elif count == 1:
        months = round(months / 10)
        if months != 0:
            print("It will take {} years and {} months to repay this loan!".format(years, months))
            print("count == 1")
        elif months == 0:
            print("It will take {} years to repay this loan!".format(years))
        print("count == 1")
    elif count == 0:
        months = 0
        months = round(months)
        if years > 1:
            print("It will take {} years to repay this loan!".format(years))
        elif years == 1:
            print("It will take {} year to repay this loan!".format(years))
        print("count == 0")
    if n == 12 or n == 12.0 or n == 12.00:
        print("It will take 1 year to repay this loan!")



