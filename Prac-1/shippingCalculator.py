total_items = int(input("please enter how many items you wish to calculate"))
total_cost = 0.0
items = []
while total_items <= 0:
    total_items = int(input("You have entered and invalid number \nPlease re-enter how many items you wish to calculate"))
for i in range(0,(total_items), 1):
    item_price = float(input("Please enter item amount"))
    total_cost = item_price + total_cost
    items.append(item_price)
for i in range(0,(total_items), 1):
    print("Price of item: " +str(items[i]))
if total_cost > 100:
    print(total_cost - total_cost / 100 * 10)
else:
    print("The total price of " +str(total_items)+" items is " +str(total_cost))

