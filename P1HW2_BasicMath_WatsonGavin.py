# Basic Math Caclulator
# 9-28-2021
# CTI-110- P1HW2-Basic Math
# Gavin Watson
tax = float(0.06)
year = float(12.0)
mTax = int
expense = input('What is the name of your expense?')
mCharge = float(input ('How much are you charged monthly for this expense?'))
mTax = tax * mCharge
Total = (mTax + mCharge) * year
dollarSign = '$'
print('Bill:', expense,'--------- Before Tax:',dollarSign,mCharge)
print ('Montly Tax:','$', mTax)
print ('Montly Charge:','$', mCharge)
print ('Annual Charge:','$', Total)

