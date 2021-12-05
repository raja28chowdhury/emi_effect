from builtins import input
from calendar import month

print("we will calculate emi feel")

inflation = float(input("tell me the inflation rate "))
inflation = 1- (inflation/100)

duration = int(input("tell me the duration in years "))

monthly_emi = int(input("tell me monthly emi "))

yearly_emi = monthly_emi*12

actual_payout_inflation_adjusted = 0


for i in range(duration):
    actual_payout_inflation_adjusted = actual_payout_inflation_adjusted + yearly_emi
    print(yearly_emi)
    yearly_emi = yearly_emi*inflation

print(actual_payout_inflation_adjusted)