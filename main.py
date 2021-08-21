

print("Enter Hourly Rate Of Pay:")
payRate = float(input())


print('Enter Hours Worked: ')
hours = float(input())


print("Enter Tax Amount As a Percentage:")
taxPer = input()

def tax(X):
    return float(X.strip('%'))/100      # Lets Just Put This Here So Our Taxes Are Together


otRate = payRate / 2 + payRate          #Assumes Overtime is Time and a Half


if hours > 40:
    otHours = hours - 40
    hours = 40
else:
    otHours = .001                      # If Time Isnt Over 40 Then Set otHours to .001


payCalc = hours * payRate               # Hours Worked Multiplied By Pay Rate
otCalc = otHours * otRate               # Overtime Hours Multiplied By Overtime Rate


if otHours >= .05:                      # If there no overtime then otHours is set to .001 so jump to else
    pay = otCalc + payCalc
else:
    pay = payCalc


taxedAmount = pay * tax(taxPer)
afterTaxPay = pay - taxedAmount

print("")                                                       # Nice Little Terminal Break
print("Pay Before Taxes: $", pay)
print("Tax Amount Deducted From Pay: $", taxedAmount)
print("Your TakeHome Pay is: $", afterTaxPay)
print("")                                                       # Another Nice Little Terminal Break
