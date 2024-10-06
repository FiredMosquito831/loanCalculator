import sys
args = sys.argv
print("This program does the sum of 2 numbers")
if len(args) != 3:
    print("This program is supposed to do the sum of 2 args values(2 numbers) and print the result")
else:
    num1 = int(args[1])
    num2 = int(args[2])
    suma = num1 + num2
    print("The sum of " + args[1] + " and " + args[2] + " is going to be " + str(suma))
