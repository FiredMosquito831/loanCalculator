import argparse
import math
# Setting up the command-line parameters
parser = argparse.ArgumentParser(description="This is a loan calculator")
parser.add_argument("--principal", type=float)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
parser.add_argument("--type")
parser.add_argument("--payment", type=float)

# Parsing parameters
args = parser.parse_args()


# Parameter error checker
def param_checker():
    # Incorrect type
    if args.type not in ["diff", "annuity"]:
        print("Incorrect parameters")
        quit()
    # Diff but payment given
    if args.type == "diff" and args.payment is not None:
        print("Incorrect parameters")
        quit()
    # No interest
    if args.interest is None:
        print("Incorrect parameters")
        quit()
    # Negative principal
    if args.principal is not None:
        if args.principal < 0:
            print("Incorrect parameters")
            quit()
    # Negative periods
    if args.periods is not None:
        if args.periods < 0:
            print("Incorrect parameters")
            quit()
    # Negative payment
    if args.payment is not None:
        if args.payment < 0:
            print("Incorrect parameters")
            quit()
    # Negative interest
    if args.interest < 0:
        print("Incorrect parameters")
        quit()


# What calculator to use based on parameters?
def calc_choice():
    if args.type == "diff":
        return diff_payment(args.principal, args.periods, interest_nominal)
    elif args.payment is None:
        return a_payment(args.principal, args.periods, interest_nominal)
    elif args.periods is None:
        return a_periods(args.principal, args.payment, interest_nominal)
    elif args.principal is None:
        return a_principal(args.payment, args.periods, interest_nominal)


# Diff annuity calculator
def diff_payment(principal, periods, interest):
    m = 1    # current month
    counter = 0
    suma_val = 0
    e_list = []
    for e in range(1, periods + 1, 1):
        Dm = (principal // periods) + interest * (principal - ((principal * (m - 1)) // periods))
        m += 1
        k = Dm - round(Dm)
        k = round(k * 10)
        if k > 1:
            Dm = round(Dm) + 1
            print("Month {}: payment is {}".format(m - 1, Dm))
        else:
            Dm = round(Dm)
            print("Month {}: payment is {}".format(m - 1, Dm))
        e_list.append(Dm)
    nr_elem = len(e_list)
    for mn in range(1, nr_elem + 1, 1):
        suma_val = suma_val + e_list[counter]
        counter += 1
    overpayment = abs(principal - suma_val)
    print("")
    print("Overpayment = {}".format(round(overpayment)))


# Annuity periods calculator
def a_periods(principal, payments, interest):
    periods = math.log(payments / (payments - interest * principal), 1 + interest)
    extra_periods = math.ceil(periods) % 12
    years = math.ceil(periods) // 12
    overpayment = abs(math.ceil(principal - (payments * periods)))
    if years == 0:
        print(""""It will take {} months to repay this loan!
        Overpayment = {}""".format(extra_periods, overpayment))
    elif extra_periods == 0:
        print("""It will take {} years to repay this loan!
        Overpayment = {}""".format(years, overpayment))
    else:
        print("""It will take {} years and {} months to repay this loan!
        Overpayment = {}""".format(years, extra_periods, overpayment))



# Annuity payment calculator
def a_payment(principal, periods, interest):
    payments = principal * ((interest * pow(1 + interest, periods)) / (pow(1 + interest, periods) - 1))
    overpayment = abs(math.ceil(principal - (payments * periods)))
    print("""Your monthly payment = {}
    Overpayment = {}""".format(math.ceil(payments), overpayment))
    payment = [payments, overpayment and overpayment, payments]


# Annuity payment calculator
def a_principal(payments, periods, interest):
    principal = payments / (interest * pow(1 + interest, periods) / (pow(1 + interest, periods) - 1))
    overpayment = math.ceil(principal - (payments * periods))
    print("""Your loan principal = {}
    Overpayment = {}""".format(math.ceil(principal), overpayment))



# 1 - check if everything is peachy with the parameters
param_checker()
# 2 - convert interest rate from percent to monthly float
interest_nominal = args.interest / 100 / 12
# 3 - select and run the calculator
calc_choice()
