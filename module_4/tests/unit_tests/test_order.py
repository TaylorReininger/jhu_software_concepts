import re

import pytest

from src.order import Order
from src.pizza import Pizza


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
    assert True



@pytest.mark.order
def test_str():

    gpa = re.search(r'GPA \d+\.[0-9]+', row[6])


    assert True



@pytest.mark.order
def test_order_paid():
    assert True







