import re

import pytest

from src.order import Order


@pytest.fixture
@pytest.mark.order
def test_init():

    # Creat an Order object
    o = Order()

    # Ensure the pizzas class member is of type "list"
    assert isinstance(o.pizzas, list)

    # Ensure that the cost class member is initialized at zero
    assert o.cost == 0

    # Ensure that the paid class member is initialized to "False"
    assert o.paid == False
    

@pytest.fixture
@pytest.mark.order
def test_input_pizza():
    
    # Create Order object and store the cost
    o = Order()
    cost1 = o.cost

    # Add a pizza to the order and check the cost again
    o.input_pizza(crust='thick', sauce='marinara', cheese='mozzarella', toppings=['pepperoni', 'mushrooms'])
    cost2 = o.cost

    # Ensure that the cost of the order increases
    assert cost2 - cost1 > 0



@pytest.mark.order
def test_str():

    # Create order object and put a pizza in the order
    o = Order()    
    o.input_pizza(crust='thick', sauce='marinara', cheese='mozzarella', toppings=['pepperoni', 'mushrooms'])
    
    # Get the order string from the __str__ method
    text = o.__str__()

    # Ensure the crust is displayed correctly
    crust = re.search('Crust: [a-zA-Z]+', text)
    assert crust

    # Ensure the sauce is displayed correctly (in a list, despite not being inserted as a list)
    sauce = re.search(r'Sauce: \[\'[a-zA-Z]+\'\]', text)
    assert sauce

    # Ensure the cheese is displayed correctly
    cheese = re.search('Crust: [a-zA-Z]+', text)
    assert cheese

    # Ensure the toppings are displayed correctly (as a list)
    toppings = re.search(r'Crust: \[\'[a-zA-Z]+\' , \'[a-zA-Z]+\'\]', text)
    assert toppings



@pytest.mark.order
def test_order_paid():
    
    # Create order object and put a pizza in the order
    o = Order()    
    o.input_pizza(crust='thick', sauce='marinara', cheese='mozzarella', toppings=['pepperoni', 'mushrooms'])

    # Use the order_paid method to mark the order as paid
    o.order_paid()

    # Ensure that the paid class member is initialized to "False"
    assert o.paid == True







