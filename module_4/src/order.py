
from typing import Union, List, Optional, Dict

from src.pizza import Pizza


class Order:

    def __init__(self) -> None:
        """
        Initializes an Order class object
        """

        # Store class members
        self.pizzas = []
        self.cost = 0
        self.paid = False
    
    
    def __str__(self):
        """
        Turns the order details into a string that can be displayed to the user. 

        :return: A single string with all the content of the order and the price
        :rtype: str
        """

        # Initialize the output string
        output = ''

        # Print out all the pizzas in the order
        for p in self.pizzas:
            output += p.__str__()
            output += '\n'

        # Display the total price
        output += '-------------------------------------------------\n'
        output += 'Total: %d'%(self.cost)

        # Return to user
        return output
    
    
    def input_pizza(self, crust: str='thin', sauce: Union[str, List]='marinara', cheese: Union[str, None]=None, toppings: Union[str, List]=['pepperoni']) -> None:
        """
        Adds a pizza to the order with the desired toppings. 

        :param crust: The type of pizza crust (thin, thick, gluten free). Must pick one. 
        :type crust: str
        :param sauce: The type of pizza sauce (marinara, pesto, liv sauce). Must pick one to multiple. 
        :type sauce: Union[str, List]
        :param cheese: The type of pizza cheese (mozzarela, None). Can pick up to one. 
        :type cheese: Union[str, None]
        :param toppings: The type of pizza toppings (pineapple, pepperoni, mushrooms). Must pick one to multiple. 
        :type toppings: Union[str, List]
        """
        
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