

from typing import Union, List, Optional, Dict



class Pizza:
    """
    The pizza object which contains all the ingredients and the associated 
    cost, as well as some useful methods. 
    """

    def __init__(self, 
            crust: str='thin', 
            sauce: Union[str, List]='marinara', 
            cheese: Union[str, None]=None, 
            toppings: Union[str, List]=['pepperoni']) -> None:
        """
        Creates a pizza object with the desired toppings. 

        :param crust: The type of pizza crust (thin, thick, gluten free). Must pick one. 
        :type crust: str
        :param sauce: The type of pizza sauce (marinara, pesto, liv sauce). Must pick one to multiple. 
        :type sauce: Union[str, List]
        :param cheese: The type of pizza cheese (mozzarela, None). Can pick up to one. 
        :type cheese: Union[str, None]
        :param toppings: The type of pizza toppings (pineapple, pepperoni, mushrooms). Must pick one to multiple. 
        :type toppings: Union[str, List]
        """

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
        """
        Turns the pizza details into a string that can be displayed to the user. 

        :return: A single string with all the content of the pizza and the price
        :rtype: str
        """

        # Create a string with the pizza information
        text = "Crust: %s, Sauce: %s, Cheese: %s, Toppings: %s, Cost: %d"%(
            self.pizza['crust'], 
            self.pizza['sauces'], 
            self.pizza['cheese'], 
            self.pizza['toppings'],
            self.price
            )

        return text

    def _tally(self) -> None:
        """
        A private method to help tally up the cost of the pizza based on the 
        chosen ingredients. 
        """

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
        """
        Gets the cost of the pizza. 

        :return: The cost of the pizza in dollars
        :rtype: int
        """

        # Simply return the cost
        return self.price


