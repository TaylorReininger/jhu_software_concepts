import re

import pytest

from src.pizza import Pizza


@pytest.mark.pizza
def test_init():

    # Initialize a pizza object and 
    p = Pizza(crust='thick', sauce='marinara', cheese='mozzarella', toppings=['pepperoni', 'mushrooms'])
    # Ensure that the price of the pizza has gone up
    assert p.price > 0



@pytest.mark.pizza
def test_str():


    # Initialize a pizza object and 
    p = Pizza(crust='thick', sauce='marinara', cheese='mozzarella', toppings=['pepperoni', 'mushrooms'])

    # Assess the __str__ method
    text = p.__str__()

    # Ensure the crust is displayed correctly
    crust = re.search('Crust: [a-zA-Z]+', text)
    assert crust

    # Ensure the sauce is displayed correctly (in a list, despite not being inserted as a list)
    sauce = re.search(r'Sauce: \[\'[a-zA-Z]+\'\]', text)
    assert sauce

    # Ensure the cheese is displayed correctly
    cheese = re.search('Cheese: [a-zA-Z]+', text)
    assert cheese

    # Ensure the toppings are displayed correctly (as a list)
    toppings = re.search(r'Toppings: \[\'[a-zA-Z]+\', \'[a-zA-Z]+\'\]', text)
    assert toppings

    # Ensure the cost is displayed correctly
    cost = re.search('Cost: [0-9]+', text)
    assert cost



@pytest.mark.pizza
def test_cost():

    # Initialize a pizza object and 
    p = Pizza(crust='thick', sauce='marinara', cheese='mozzarella', toppings=['pepperoni', 'mushrooms'])

    # Get the cost of the pizza from the object
    c = p.cost()

    # Ensure that the pizza costs something
    assert c > 0



