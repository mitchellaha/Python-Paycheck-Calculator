
payRate = float(input("Enter Hourly Rate Of Pay: "))
hours = float(input("Enter Hours Worked: "))
taxPer = input("Enter Tax Amount As a Percentage: ")

otRate = payRate / 2 + payRate  # Assumes Overtime is Time and a Half
otHours = hours - 40  # Math For Overtime / Anything Over 40 Hours Is Overtime


def tax(taxPer):  # Removed The Percentage Symbol If It Was Included
    return float(taxPer.strip('%'))/100


def pay(hours, payRate):  # Pay Function
    if hours > 40:
        # If There Is Overtime then Calculate The Pay (40*HR)+(OT*(HR/2)+HR)
        return float((40 * payRate) + (otHours * otRate))
    else:
        # If No Overtime Then Just Do The Regular HR*Rate
        return float(hours * payRate)


taxedAmount = pay(hours, payRate) * tax(taxPer)
afterTaxPay = pay(hours, payRate) - taxedAmount

print("\n", "Before Taxes:  $", pay(hours, payRate))
print(" Tax Deduction: $", taxedAmount)
print(" After Taxes:   $", afterTaxPay, "\n")
