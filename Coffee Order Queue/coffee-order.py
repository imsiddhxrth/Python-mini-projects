total_price = 0.0
drink_count = 0
while True:
    name = input("Enter customer's name (or 'done' to finish): ")
    if name.lower() == "done":
        break

    drink_order = input("What drink would you like? (latte, americano, espresso): ").lower()

    if drink_order == "latte":
        total_price += 3.50
        drink_count += 1
    elif drink_order == "americano":
        total_price += 3.00
        drink_count += 1
    elif drink_order == "espresso":
        total_price += 2.50
        drink_count += 1
    else:
        print("Sorry, we don't have that drink. Please try again.")
        continue

print(f"Total drinks ordered: {drink_count}")
print(f"Total price: ${total_price:.2f}")