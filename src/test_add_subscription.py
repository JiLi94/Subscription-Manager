import pytest
from add_subscription_for_testing import add_sub

new_sub = add_sub()
subscription = new_sub[1]

def test_charge_is_positive_number():
    assert subscription['Charge'] > 0
 