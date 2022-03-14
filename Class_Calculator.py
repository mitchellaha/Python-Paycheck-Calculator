# Also Another Calculator, But Make it Classy

class calculator:
    def __init__(self):
        self.hours = 0
        self.rate = 0
        self.tax = 0
        self.basepay = 0
        self.taxamount = 0
        self.afterTax = 0

    def inputs(self):
        self.rate = float(input("Enter rate: "))
        self.hours = float(input("Enter hours: "))
        self.tax = float(input("Enter tax rate: "))
        return self.hours, self.rate, self.tax

    def basePay(self):
        if self.hours > 40:
            self.otRate = self.rate / 2 + self.rate
            self.otHours = self.hours - 40
            self.basepay = (40 * self.rate) + (self.otHours * self.otRate)
        else:
            self.basepay = self.hours * self.rate
        return self.basepay

    def taxCalc(self):
        self.tax = self.tax / 100
        self.taxamount = self.basepay * self.tax
        return self.taxamount

    def payCalc(self):
        self.afterTax = self.basepay - self.taxamount
        return self.afterTax

    def fancyPrint(self):
        print(" Before Taxes:  $", self.basepay)
        print(" Tax Deduction: $", self.taxamount)
        print(" After Taxes:   $", self.afterTax)

    def main(self):
        self.inputs()
        self.basepay = self.basePay()
        self.taxamount = self.taxCalc()
        self.afterTax = self.payCalc()
        self.fancyPrint()


if __name__ == "__main__":
    calc = calculator()
    calc.main()