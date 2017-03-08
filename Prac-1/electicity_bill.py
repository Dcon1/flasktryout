TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
print("Electicity bill estimator 2.0")
tariff_choice = int(input("which tariff are you on 11 or 31"))
if tariff_choice == 11:
    tariff = TARIFF_11
else:
    tariff = TARIFF_31
total_daily_kwh = float(input("Please enter daily kWh usage"))
billing_days = int(input("Please Enter total of billing days"))
estimate_bill = tariff  * total_daily_kwh * float(billing_days)
print(round(estimate_bill, 2))
