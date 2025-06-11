
import pytest

from src.order import Order


@pytest.mark.order
@pytest.mark.pizza
def test_multiple_pizzas():

    # Create an order object
    o = Order()
    assert o.cost() == 0
    # Input the default pizza
    o.input_pizza()
    cost1 = o.cost
    assert cost1 > 0

    # Input another pizza
    o.input_pizza()
    cost2 = o.cost
    assert cost2 > cost1
    
    # Input another pizza
    o.input_pizza()
    cost3 = o.cost
    assert cost3 > cost2






