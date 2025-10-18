#Customer class unit test
from unittest.mock import Mock
from lib.customer import *
from lib.takeaway import *
import pytest

"""
given a name, address, phone 
should initialize name, address and phone
"""
def test_given_name_address_phone_should_initialize_these_properties():
    takeaway = Takeaway()
    customer = Customer("John Mayer", "71 Mayfair Street", "123456789101", takeaway)
    assert customer.name == "John Mayer"
    assert customer.address ==  "71 Mayfair Street"
    assert customer.phone == "123456789101"
    assert customer.takeaway == takeaway


"""
view_menu function returns menu in string format
"""
def test_view_menu_returns_menu_in_string_format():
    takeaway = Takeaway()
    customer = Customer("John Mayer", "71 Mayfair Street", "123456789101", takeaway)
    assert customer.view_menu() == "burger, price:5.80\nfries, price:1.80\npizza, price:9.00\nhalloumi fries, price:7.00\nsirloin steak, price:16.99"

"""
add_dish without quantity adds dish to customer selected list with a quantity of 1
note: quantity is an optional parameter with a default value of 1
"""
def test_given_dish_without_quantity_adds_dish_with_quantity_of_1():
    takeaway = Takeaway()
    customer = Customer("John Mayer", "71 Mayfair Street", "123456789101", takeaway)
    customer.add_dish("halloumi fries")
    assert customer.customer_selected_dishes == [{"dish name":"halloumi fries", "price": 7, "quantity": 1}]


"""
multiple same add_dish without quantity adds dish to customer selected list and increases quantity as necessary
"""
def test_given_same_dish_without_quantity_adds_dish_with_necessary_quantity():
    takeaway = Takeaway()
    customer = Customer("John Mayer", "71 Mayfair Street", "123456789101", takeaway)
    customer.add_dish("halloumi fries")
    customer.add_dish("halloumi fries")
    assert customer.customer_selected_dishes == [{"dish name":"halloumi fries", "price": 7, "quantity": 2}]


"""
multiple different add_dish without quantity adds different dish to customer selected list with a quantity of 1
"""
def test_given_different_dish_without_quantity_adds_dish_with_quantity_of_1():
    takeaway = Takeaway()
    customer = Customer("John Mayer", "71 Mayfair Street", "123456789101", takeaway)
    customer.add_dish("halloumi fries")
    customer.add_dish("fries")
    assert customer.customer_selected_dishes == [{"dish name":"halloumi fries", "price": 7, "quantity": 1}, {"dish name":"fries", "price": 1.80, "quantity": 1}]


"""
add_dish with quantity adds dish to customer selected list with the given quantity
"""
def test_given_dish_with_quantity_adds_dish_with_given_quantity():
    takeaway = Takeaway()
    customer = Customer("John Mayer", "71 Mayfair Street", "123456789101", takeaway)
    customer.add_dish("halloumi fries", 2)
    assert customer.customer_selected_dishes == [{"dish name":"halloumi fries", "price": 7, "quantity": 2}]


"""
multiple add_dish with quantity adds multiple dish to customer selected list with the given quantity
"""
def test_given_dish_with_quantity_adds_multiple_dish_with_given_quantity():
    takeaway = Takeaway()
    customer = Customer("John Mayer", "71 Mayfair Street", "123456789101", takeaway)
    customer.add_dish("halloumi fries", 2)
    customer.add_dish("sirloin steak", 2)
    assert customer.customer_selected_dishes == [{"dish name":"halloumi fries", "price": 7, "quantity": 2}, {"dish name":"sirloin steak", "price": 16.99, "quantity": 2}]


"""
given if food is not on the menu
add_dish() raises error message "food not in the menu!"
add_dish() only adds dish that is in the menu
"""
def test_given_dish_is_not_on_menu_returns_error_and_only_adds_dish_that_is_in_the_menu():
    takeaway = Takeaway()
    customer = Customer("John Mayer", "71 Mayfair Street", "123456789101", takeaway)
    customer.add_dish("halloumi fries", 2)

    with pytest.raises(ValueError) as e:
        customer.add_dish("grilled salmon", 2) 
    
    assert str(e.value) == "food not in the menu!"
    assert customer.customer_selected_dishes == [{"dish name":"halloumi fries", "price": 7, "quantity": 2}]


"""
given an empty food parameter
add_dish() raises error message "Food cannot be empty!"
"""
def test_given_empty_food_parameter_raises_error():
    takeaway = Takeaway()
    customer = Customer("John Mayer", "71 Mayfair Street", "123456789101", takeaway)
    with pytest.raises(ValueError) as e:
        customer.add_dish("") 
    
    assert str(e.value) == "Food cannot be empty!"


"""
given a specified dish without quantity
remove_dish() removes specified dish if found in selected list
note: quantity is an optional parameter with a default value of 1
"""
def test_given_dish_without_quantity_remove_dish_removes_dish_if_found_in_selected_list():
    takeaway = Takeaway()
    customer = Customer("John Mayer", "71 Mayfair Street", "123456789101", takeaway)
    customer.add_dish("halloumi fries")
    customer.remove_dish("halloumi fries")
    assert customer.customer_selected_dishes == []


"""
given a specified dish without quantity
remove_dish() throws error message if food not found in the menu or not in selected list
"""
def test_given_dish_without_quantity_throws_error_if_food_not_in_selected_list():
    takeaway = Takeaway()
    customer = Customer("John Mayer", "71 Mayfair Street", "123456789101", takeaway)
    customer.add_dish("halloumi fries")
    with pytest.raises(ValueError) as e:
        customer.remove_dish("curly fries")
    assert str(e.value) == "Food not found. So cannot be removed"


"""
given a specified dish with quantity
remove_dish() removes the dish and corrects the quantity
"""
def test_given_dish_with_quantity_removes_dish_and_corrects_quantity():
    takeaway = Takeaway()
    customer = Customer("John Mayer", "71 Mayfair Street", "123456789101", takeaway)
    customer.add_dish("halloumi fries", 3)
    customer.remove_dish("halloumi fries", 2)
    assert customer.customer_selected_dishes == [{"dish name":"halloumi fries", "price": 7, "quantity": 1}]


"""
given a specified dish with quantity more than what is in the selected_dish list
remove_dish() delete the specified dish
"""
def test_given_specified_dish_with_quantity_more_than_what_is_in_the_selected_list_removes_item():
    takeaway = Takeaway()
    customer = Customer("John Mayer", "71 Mayfair Street", "123456789101", takeaway)
    customer.add_dish("halloumi fries", 3)
    customer.remove_dish("halloumi fries", 4)
    assert customer.customer_selected_dishes == []