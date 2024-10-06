print("Enter the loan principal: ")
f = 0
loan_principal = int(input())
print("What do you want to calculate? ")
decision = input('''type "m" - for the number of monthly payments,
type "p" - for the monthly payment: ''')
if decision == "m":
    monthly_payment = int(input("Enter monthly payment: "))
    if (loan_principal / monthly_payment) % 10 != 0 and (loan_principal / monthly_payment) % 10 != 1:
        time_to_pay = loan_principal // monthly_payment
        print("It will take", time_to_pay, "months to pay the loan")
    elif (loan_principal / monthly_payment) == 1:
        time_to_pay = loan_principal // monthly_payment
        print("It will take", time_to_pay, "month to pay the loan")
    else:
        time_to_pay = loan_principal // monthly_payment + 1
        print("It will take", time_to_pay, "months to pay the loan")
elif decision == "p":
    time_to_pay = int(input("Enter the number of months: "))
    if (loan_principal / time_to_pay) % 10 == 0:
        monthly_payment = loan_principal // time_to_pay
        print("Your monthly payment =", monthly_payment)
    elif loan_principal // time_to_pay == 1:
        monthly_payment = loan_principal / time_to_pay
        print("Your monthly payment =", monthly_payment)
    elif loan_principal / time_to_pay and isinstance(loan_principal / time_to_pay, float):
        monthly_payment = loan_principal // time_to_pay + 1
        last_payment = loan_principal - (time_to_pay - 1) * monthly_payment
        monthly_payment = str(monthly_payment)
        last_payment = str(last_payment)
        print("Your monthly payment = " + monthly_payment, "and the last payment = "+ last_payment + ".")





