from fastapi import FastAPI
from starlette.responses import FileResponse 
from pydantic import BaseModel
import os

# Current Directory
dir_path = os.path.dirname(os.path.realpath(__file__))

app = FastAPI()

class PaycheckTool:
    def __init__(self, hourly_rate: float, tax_rate: float):
        self.hourly_rate = hourly_rate
        self.tax_rate = tax_rate

    def setPayRate(self, pay_rate: float):
        self.hourly_rate = pay_rate

    def setTaxRate(self, tax_rate: float):
        self.tax_rate = tax_rate

    def taxDeductionAmount(self, pay):
        tax = self.tax_rate / 100
        return round(pay * tax, 2)


    def grossPay(self, hours):
        if hours > 40:
            ot_rate = self.hourly_rate / 2 + self.hourly_rate
            ot_hours = hours - 40
            return (40 * self.hourly_rate) + (ot_hours * ot_rate)
        else:
            return hours * self.hourly_rate

    def netPay(self, hours):
        gross_pay = self.grossPay(hours)
        tax_amount = self.taxDeductionAmount(gross_pay)
        return round(gross_pay - tax_amount, 2)


class PayRate(BaseModel):
    pay_rate: float
    tax_rate: float

class PaycheckReturn(BaseModel):
    grossPay: float
    taxDeduct: float
    netPay: float

@app.get("/")
async def read_index():
    return FileResponse(dir_path + '/index.html')

@app.get("/main/")
def mainTool(hourly_rate: float, tax_rate: float, hours: float):
    tool = PaycheckTool(0, 0)
    tool.setPayRate(hourly_rate), tool.setTaxRate(tax_rate)
    gross = tool.grossPay(hours)
    return PaycheckReturn(
        grossPay=gross,
        taxDeduct=tool.taxDeductionAmount(gross),
        netPay=tool.netPay(hours)
    )


tool = PaycheckTool(0, 0)

@app.post("/SetRate/")
def setRate(pay_rate: float, tax_rate: float):
    tool.setPayRate(pay_rate)
    tool.setTaxRate(tax_rate)
    return {"Status": "Success"}

@app.get("/GetRate/")
def getRate():
    return {"PayRate": tool.hourly_rate, "TaxRate": tool.tax_rate}

@app.get("/GrossPay/")
def grossPay(hours: float):
    return {"GrossPay": tool.grossPay(hours)}

@app.get("/NetPay/")
def getNet(hours: float):
    return {"Net": tool.netPay(hours)}
