monthly_totals = []
months = int(input("Please enter number of months"))
for i in range(1,months + 1 ,1):
    monthly_income = int(input("Enter income for month {}: ".format(i)))
    monthly_totals.append(monthly_income)
for i in range(1,months + 1 ,1):
    print("Month {0:>2} - Income: $ {1:>10,.2f} Total: $ {1:>10,.2f}".format(i,monthly_totals[i-1]))