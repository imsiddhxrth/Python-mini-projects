purse = 5000
class Pizza:
    valid_sizes = ["small", "medium", "large"]
    valid_crusts = ["thin", "thick", "cheese burst", "pan pizza"]
    valid_toppings = ["pepperoni", "mushrooms", "onions", "sausage", "bacon", "extra cheese", "black olives", "green peppers", "pineapple", "spinach"]
    size_prices = {"small": 50, "medium": 100, "large": 150}
    crust_prices = {"thin": 50, "thick": 100, "cheese burst": 100, "pan pizza": 50}
    topping_price = 10
    def __init__(self, size, crust, toppings):
        self.size = size
        self.crust = crust
        self.toppings = toppings
    def add_toppings(self, toppings):
        self.toppings.extend(toppings)
    def remove_toppings(self, toppings):
        for topping in toppings:
            if topping in self.toppings:
                self.toppings.remove(topping)
            else:
                print(f"{topping} is not on the pizza.")
    def print_details(self):
        print(f'size : {self.size}')
        print(f'crust : {self.crust}')
        if self.toppings:
            print(f'toppings : {self.toppings}')
        else:
            print('no toppings yet')
number_of_pizzas = int(input("How many pizzas would you like to order?: "))
pizzas = []
for i in range(number_of_pizzas):
    size = input("Enter the size of the pizza (small, medium, large): ")
    while size not in Pizza.valid_sizes:
        print("Invalid size. Please enter small, medium, or large.")
        size = input("Enter the size of the pizza (small, medium, large): ")
    crust = input("Enter the type of crust (thin, thick, cheese burst, pan pizza): ")
    while crust not in Pizza.valid_crusts:
        print("Invalid crust. Please enter thin, thick, cheese burst, or pan pizza.")
        crust = input("Enter the type of crust (thin, thick, cheese burst, pan pizza): ")
    toppings = []
    while True:
        add_more_toppings = input("Would you like to add toppings? (yes/no): ")
        if add_more_toppings.lower() == "yes" or add_more_toppings.lower() == "no":
            break
        print("Please enter yes or no.")
    while add_more_toppings.lower() == "yes":
        topping = input(f"Enter a topping ({', '.join(Pizza.valid_toppings)}): ")
        if topping in Pizza.valid_toppings:
            toppings.append(topping)
        else:
            print(f"Invalid topping. Valid options are: {Pizza.valid_toppings}")
        while True:
            add_more_toppings = input("Would you like to add more toppings? (yes/no): ")
            if add_more_toppings.lower() == "yes" or add_more_toppings.lower() == "no":
                break
            print("Please enter yes or no.")
    pizza = Pizza(size, crust, toppings)
    pizzas.append(pizza)
total_cost = 0
for pizza in pizzas:
    total_cost += Pizza.size_prices[pizza.size] + Pizza.crust_prices[pizza.crust] + len(pizza.toppings) * Pizza.topping_price
print(f"Total cost of the order: {total_cost}")
for pizza in pizzas:
    pizza.print_details()
confirm_order = input("Do you want to confirm the order? (yes/no): ")
if confirm_order.lower() == "yes":
    if total_cost > purse:
        print("You do not have enough money to place this order.")
    else:
        print(f"Order confirmed! Total cost: {total_cost}. Thank you for your purchase.")
        purse -= total_cost
        print(f"Remaining balance: {purse}")
else:
    print("Order cancelled.")
    print(f"Remaining balance: {purse}")