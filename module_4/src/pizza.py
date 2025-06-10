

from typing import Union, List, Optional, Dict




class Pizza:

    def __init__(self, crust: str='thin', sauce: Union[str, List]='marinara', cheese: Union[str, None]='mozzarella', toppings: Union[str, List]=['pepperoni']) -> None:

        # Store the options in a pizza dictionary
        self.pizza = dict()
        self.pizza['crust'] = crust
        # Sauces are stored as a list
        if isinstance(sauce, list):
            self.pizza['sauces'] = sauce
        else:
            self.pizza['sauces'] = [sauce]
        self.pizza['cheese'] = cheese
        # Toppings are stored as a list
        if isinstance(toppings, list):
            self.pizza['toppings'] = toppings
        else:
            self.pizza['toppings'] = [toppings]


        # Create a lookup table for pricing out the pizzas
        self.pricing = dict()
        self.pricing['thin'] = 5
        self.pricing['thick'] = 6
        self.pricing['gluten free'] = 8
        self.pricing['marinara'] = 2
        self.pricing['pesto'] = 3
        self.pricing['liv sauce'] = 5
        self.pricing['mozzarella'] = 0
        self.pricing['pineapple'] = 1
        self.pricing['pepperoni'] = 2
        self.pricing['mushrooms'] = 3

        # Initialize the price to zero
        self.price = 0

        # Tally up the price
        self._tally()


    def __str__(self) -> str:
        text = "Crust: %s, Sauce: %s, Cheese: %s, Toppings: %s, Cost: %d"%(
            self.pizza['crust'], 
            self.pizza['sauces'], 
            self.pizza['cheese'], 
            self.pizza['toppings'],
            self.price
            )

        return text

    def _tally(self) -> None:

        # Count up the cost of each part of the pizza
        # The crust
        self.price += self.pricing[self.pizza['crust'].lower()]

        # The sauces
        for sauce in self.pizza['sauces']:
            self.price += self.pricing[sauce.lower()]

        # The cheese
        if self.pizza['cheese']:
            self.price += self.pricing[self.pizza['cheese'].lower()]

        # The toppings
        for topping in self.pizza['toppings']:
            self.price += self.pricing[topping.lower()]


    def cost(self) -> int:
        # Simply return the cost
        return self.price


