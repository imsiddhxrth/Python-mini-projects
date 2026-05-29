class Pizza:
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
my_pizza = Pizza("large", "cheese burst", [])
my_pizza.add_toppings(["mushrooms"])
my_pizza.add_toppings(["onions"])
my_pizza.print_details()
    