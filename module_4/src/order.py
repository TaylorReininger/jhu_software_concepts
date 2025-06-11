
from typing import Union, List, Optional, Dict

from src.pizza import Pizza


class Order:

    def __init__(self) -> None:
        
        # Store class members
        self.pizzas = []
        self.cost = 0
        self.paid = False
    
    
    def __str__(self):
        
        # Initialize the output string
        output = ''

        # Print out all the pizzas in the order
        for p in self.pizzas:
            output += p.__str__()
            output += '\n'

        # Display the total price
        output += '-------------------------------------------------\n'
        output += 'Total: %d'%(self.cost)
        return output
    
    
    def input_pizza(self, crust: str='thin', sauce: Union[str, List]='marinara', cheese: Union[str, None]=None, toppings: Union[str, List]=['pepperoni']) -> None:

        # Make a pizza object with the specified parameters
        p = Pizza(crust=crust, sauce=sauce, cheese=cheese, toppings=toppings)

        # Get the cost of this pizza
        this_cost = p.cost()

        # Log these parameters as class members
        self.pizzas.append(p)
        self.cost += this_cost



    def order_paid(self) -> None:
        # Change the paid member to True
        self.paid = True