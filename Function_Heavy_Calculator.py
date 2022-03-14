# just another way to do a paycheck calculator, but with
# heavy reliance on functions

def inputs():
    rate = float(input("Enter rate: "))
    hours = float(input("Enter hours: "))
    tax = float(input("Enter tax rate: "))
    return hours, rate, tax

def basePay(hours, rate):
    if hours > 40:
        otRate = rate / 2 + rate
        otHours = hours - 40
        return (40 * rate) + (otHours * otRate)
    else:
        return hours * rate

def taxCalc(basepay, tax):
    tax = tax / 100
    taxAmount = basepay * tax
    return taxAmount

def payCalc(basepay, taxamount):
    return basepay - taxamount

def fancyPrint(beforeTax, taxDeduction, afterTax):
    print(" Before Taxes:  $", beforeTax)
    print(" Tax Deduction: $", taxDeduction)
    print(" After Taxes:   $", afterTax)

def main():
    hours, rate, tax = inputs()
    basepay = basePay(hours, rate)
    taxamount = taxCalc(basepay, tax)
    afterTax = payCalc(basepay, taxamount)
    fancyPrint(basepay, taxamount, afterTax)

if __name__ == "__main__":
    main()
