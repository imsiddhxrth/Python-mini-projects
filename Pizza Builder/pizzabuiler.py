class Pizza:
    valid_sizes = ["small", "medium", "large"]
    valid_crusts = ["thin", "thick", "cheese burst", "pan pizza"]
    valid_toppings = ["pepperoni", "mushrooms", "onions", "sausage", "bacon", "extra cheese", "black olives", "green peppers", "pineapple", "spinach"]
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
number_of_pizzas = int(input("How many pizzas would you like to order? "))
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
    add_more_toppings = input("Would you like to add toppings? (yes/no) ")
    while add_more_toppings.lower() == "yes":
        topping = input("Enter a topping: ")
        if topping in Pizza.valid_toppings:
            toppings.append(topping)
        else:
            print(f"Invalid topping. Valid options are: {Pizza.valid_toppings}")
        add_more_toppings = input("Would you like to add more toppings? (yes/no) ")
    pizza = Pizza(size, crust, toppings)
    pizzas.append(pizza)
for pizza in pizzas:
    pizza.print_details()