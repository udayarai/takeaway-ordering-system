# Takeaway, Customer Multi-Class Planned Design Recipe

## 1. Describe the Problem

As a customer
So that I can check if I want to order something
I would like to see a list of dishes with prices.

As a customer
So that I can order the meal I want
I would like to be able to select some number of several available dishes.

As a customer
So that I can verify that my order is correct
I would like to see an itemised receipt with a grand total.

As a customer
So that I am reassured that my order will be delivered on time
I would like to receive a text such as "Thank you! Your order was placed and will be delivered before 18:52" after I have ordered.

## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```
see drawing.excalidraw
```

_Also design the interface of each class in more detail._

```python
class Takeaway: #Main class
    # User-facing properties:
    #   None

    def __init__():
        # Parameters:
        #   None
        # Self instance variable:
        #   self.all_customer_orders = [] #list that stores all customer_orders
        #   for e.g. {customer1 : [{"dish name" : "burger", "price" : 5.80, "quantity": 1}, {"dish name" : "fries", "price" : 1.80, "quantity": 1}]
        pass # No code here yet

    def get_menu(self):
        #Returns
        #   returns a list with dictionaries for e.g. see below
        #   [{"dish_name" : "burger", "price" : 5.80}, {"dish_name": "fries", "price" : 1.80}]
        pass # No code here yet

    def add_customer_order(self, customer):
        # Parameters:
        #   customer: an instance of Customer
        #   self.customer = customer
        # Side-effects:
        #   Adds the customer order to self.all_customer_orders of the self object
        pass # No code here yet

    def verify_order(self):
        # Parameters:
        #   None
        # Returns:
        #   An itemised recipt with total
        #   for e.g.
        #   Food    Qty Price 
        #   Burger  1   1.50
        #   Pizza   2   2
        #
        #   Total   3.50
        pass # No code here yet

    def generate_timestamp_sms_message(self):
        # Parameters:
        #   None
        # Returns:
        #   String with message "Thank you! Your order was placed and will be delivered before 18:52" 
        pass # No code here yet

    def send_sms_message(self):
        # Parameters:
        #   None
        # Returns:
        #   Sends sms message to the customer using vonage package
        pass # No code here yet


#CLASS CUSTOMER
class Customer:
    # User-facing properties:
    #   name: string
    #   address: string
    #   phone: string

    def __init__(self, name, address, phone, takeaway):
        # Parameters:
        # name: string
        # address: string
        # phone: string
        # takeaway: object instance of takeaway class
        # Side-effects:
        #   Sets the name, address and phone of the customer
        #self.name = name
        #self.address = address
        #self.phone = phone
        #self.takeaway = takeaway
        #
        # Class instance variable
        #   self.customer_selected_dishes = []  #list to store customer selected dishes
        #   for e.g. [{"dish name":"burger", "price": 4, "qty": 1}, ...]
        pass # No code here yet

    def view_menu(self):
        #Parameters:
        #   None
        #Returns menu in string format
        #   for e.g. halloumi fries, price: 7 etc

    def add_dish(self, dish, quantity=1):
        #Parameters:
        #   dish: string representing name of dish for e.g. burger
        #   quantity: integer representing quantity of dish e.g. 1, 2, 3, etc
        # Side-effects:
        #   Adds the customer selected dishes to self.customer_selected_dishes of the self object
        pass # No code here yet

    def remove_dish(self, dish, quantity=1):
        #Parameters:
        #   dish: string representing name of dish for e.g. burger
        #   quantity (optional default=1): integer representing quantity of dish e.g. 1, 2, 3, etc
        # Side-effects:
        #   Removes the customer selected dishes from self.customer_selected_dishes of the self object
        pass # No code here yet
"""

```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# Takeaway class Integration tests

"""
given a customer instance
where customer has selected multiple dishes
add_customer_order adds all customer order to self.all_customer_orders
"""
customer = Customer("John Mayer", "71 Mayfair Street", "123456789101")
customer.add_dish("Burger", 1)
customer.add_dish("fries", 1)

takeaway = Takeaway()
takeaway.add_customer_order(customer)
takeaway.all_customer_orders #=> {"John Mayer" : [{"dish name" : "burger", "price" : 5.80, "quantity": 1}, {"dish name" : "fries", "price" : 1.80, "quantity": 1}]}


"""
given a customer instance
where customer has selected the dishes
add_customer_order has added the customer order to self.all_customer_orders
verify shows the itemised receipt with total
"""
customer = Customer("John Mayer", "71 Mayfair Street", "123456789101")
customer.add_dish("Burger", 1)
customer.add_dish("Fries", 1)

takeaway = Takeaway()
takeaway.add_customer_order(customer)
takeaway.verify_order() #=> "Food     Qty     Price\nBurger     1     1.50\nFries    1     1.80\nTotal     7.60"



"""
given a customer instance
where customer has selected the dishes
add_customer_order has added the customer order to self.all_customer_orders
generate_timestamp_sms_message() generates sms message
"""
customer = Customer("John Mayer", "71 Mayfair Street", "123456789101")
customer.add_dish("Burger", 1)
customer.add_dish("Fries", 1)

takeaway = Takeaway()
takeaway.add_customer_order(customer)
takeaway.generate_timestamp_sms_message() #=> "Thank you! Your order was placed and will be delivered before 18:52" 


```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# Takeaway class unit tests

"""
given a customer instance
where customer has selected multiple dishes
add_customer_order adds all customer order to self.all_customer_orders
"""
customer = Mock()
customer.name = "John Mayer"
customer.address =  "71 Mayfair Street"
customer.phone = "123456789101"

customer.add_dish("Burger", 1)
customer.add_dish("fries", 1)

takeaway = Takeaway()
takeaway.add_customer_order(customer)
takeaway.all_customer_orders #=> {"John Mayer" : [{"dish name" : "burger", "price" : 5.80, "quantity": 1}, {"dish name" : "fries", "price" : 1.80, "quantity": 1}]}


"""
customer = Mock()
customer.name = "John Mayer"
customer.address =  "71 Mayfair Street"
customer.phone = "123456789101"
"""
customer = Customer("John Mayer", "71 Mayfair Street", "123456789101")
customer.add_dish("Burger", 1)
customer.add_dish("Fries", 1)

takeaway = Takeaway()
takeaway.add_customer_order(customer)
takeaway.verify_order() #=> "Food     Qty     Price\nBurger     1     1.50\nFries    1     1.80\nTotal     7.60"



"""
given a customer instance
where customer has selected the dishes
add_customer_order has added the customer order to self.all_customer_orders
generate_timestamp_sms_message() generates sms message
"""
customer = Mock()
customer.name = "John Mayer"
customer.address =  "71 Mayfair Street"
customer.phone = "123456789101"

customer.add_dish("Burger", 1)
customer.add_dish("Fries", 1)

takeaway = Takeaway()
takeaway.add_customer_order(customer)
takeaway.generate_timestamp_sms_message() #=> "Thank you! Your order was placed and will be delivered before 18:52" #18:52 is an example only 



#Customer class unit test
"""
given a name, address, phone 
should initialize name, address and phone
"""
customer = Customer("John Mayer", "71 Mayfair Street", "123456789101")
customer.name #=> "John Mayer"
customer.address #=>  "71 Mayfair Street"
customer.phone #=> "123456789101"


"""
given a takeaway instance
view_menu() returns the menu in string format
"""
customer = Customer("John Mayer", "71 Mayfair Street", "123456789101")
takeaway = Takeaway()

customer.view_menu(takeaway) #=> burger, price : 5.80\nfries, price : 1.80\npizza, price : 9\nhalloumi fries, price : 7\nsirloin steak, price: 16.99"


"""
add_dish without quantity adds dish to customer selected list with a quantity of 1
"""
customer = Customer("John Mayer", "71 Mayfair Street", "123456789101")
customer.add_dish("halloumi fries")
customer.customer_selected_dishes #=> [{"dish name":"halloumi fries", "price": 4, "qty": 1}]


"""
multiple same add_dish without quantity addsdish to customer selected list and increases quantity as necessary
"""
customer = Customer("John Mayer", "71 Mayfair Street", "123456789101")
customer.add_dish("halloumi fries")
customer.add_dish("halloumi fries")
customer.customer_selected_dishes #=> [{"dish name":"halloumi fries", "price": 4, "qty": 2}]


"""
multiple different add_dish without quantity adds different dish to customer selected list with a quantity of 1
"""
customer = Customer("John Mayer", "71 Mayfair Street", "123456789101")
customer.add_dish("halloumi fries")
customer.add_dish("fries")
customer.customer_selected_dishes #=> [{"dish name":"halloumi fries", "price": 4, "qty": 1}, {"dish name":"fries", "price": 1.80, "qty": 1}]


"""
add_dish with quantity adds dish to customer selected list with the given quantity
"""
customer = Customer("John Mayer", "71 Mayfair Street", "123456789101")
customer.add_dish("halloumi fries", 2)
customer.customer_selected_dishes #=> [{"dish name":"halloumi fries", "price": 4, "qty": 2}]


"""
multiple add_dish with quantity adds multiple dish to customer selected list with the given quantity
"""
customer = Customer("John Mayer", "71 Mayfair Street", "123456789101")
customer.add_dish("halloumi fries", 2)
customer.add_dish("sirloin steak", 2)
customer.customer_selected_dishes #=> [{"dish name":"halloumi fries", "price": 4, "qty": 2}, {"dish name":"sirlion steak", "price": 16.99, "qty": 2}]


"""
given if food is not on the menu
add_dish() raises error message "food not in the menu!"
add_dish() only adds dish that is in the menu
"""
customer = Customer("John Mayer", "71 Mayfair Street", "123456789101")
customer.add_dish("halloumi fries", 2)
customer.add_dish("grilled salmon", 2) #=> "food not in the menu!"
customer.customer_selected_dishes #=> [{"dish name":"halloumi fries", "price": 4, "qty": 2}]


"""
given an empty food parameter
add_dish() raises error message "Food cannot be empty!"
"""
customer = Customer("John Mayer", "71 Mayfair Street", "123456789101")
customer.add_dish("") #=> "Food cannot be empty!"


"""
given a specified dish without quantity
remove_dish() removes specified dish if found in selected list
"""
customer = Customer("John Mayer", "71 Mayfair Street", "123456789101")
customer.add_dish("halloumi fries")
customer.remove_dish("halloumi fries")
customer.customer_selected_dishes #=> []



"""
given a specified dish without quantity
remove_dish() throws error message if food not in selected list
"""
customer = Customer("John Mayer", "71 Mayfair Street", "123456789101")
customer.add_dish("halloumi fries")
customer.remove_dish("curly fries")
customer.customer_selected_dishes #=> "Food not found. So cannot be removed"


"""
given a specified dish with quantity
remove_dish() removes the dish and corrects the quantity
"""
customer = Customer("John Mayer", "71 Mayfair Street", "123456789101")
customer.add_dish("halloumi fries", 3)
customer.remove_dish("halloumi fries", 2)
customer.customer_selected_dishes #=> [{"dish name":"halloumi fries", "price": 4, "qty": 1}]


"""
given a specified dish with quantity more than what is in the selected_dish list
remove_dish() delete the specified dish
"""
customer = Customer("John Mayer", "71 Mayfair Street", "123456789101")
customer.add_dish("halloumi fries", 3)
customer.remove_dish("halloumi fries", 4)
customer.customer_selected_dishes #=> []

```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._

``` python
# Takeaway class Integration tests
from lib.customer import *

"""
given a customer instance
where customer has selected multiple dishes
add_customer_order adds all customer order to self.all_customer_orders
"""
def test_given_customer_instance_adds_all_customer_order():
    customer = Customer("John Mayer", "71 Mayfair Street", "123456789101")
    customer.add_dish("Burger", 1)
    customer.add_dish("fries", 1)

    takeaway = Takeaway()
    takeaway.add_customer_order(customer)
    assert takeaway.all_customer_orders == {"John Mayer" : [{"dish name" : "burger", "price" : 5.80, "quantity": 1}, {"dish name" : "fries", "price" : 1.80, "quantity": 1}]}


"""
given a customer instance
where customer has selected the dishes
add_customer_order has added the customer order to self.all_customer_orders
verify shows the itemised receipt with total
"""
def test_given_customer_instance_with_dishes_added_verify_order_shows_itemized_receipt():
    customer = Customer("John Mayer", "71 Mayfair Street", "123456789101")
    customer.add_dish("Burger", 1)
    customer.add_dish("Fries", 1)

    takeaway = Takeaway()
    takeaway.add_customer_order(customer)
    assert takeaway.verify_order() == "Food     Qty     Price\nBurger     1     1.50\nFries    1     1.80\nTotal     7.60"



"""
given a customer instance
where customer has selected the dishes
add_customer_order has added the customer order to self.all_customer_orders
generate_timestamp_sms_message() generates sms message
"""
def test_generates_sms_message_with_timestamp():
    customer = Customer("John Mayer", "71 Mayfair Street", "123456789101")
    customer.add_dish("Burger", 1)
    customer.add_dish("Fries", 1)

    takeaway = Takeaway()
    takeaway.add_customer_order(customer)
    assert takeaway.generate_timestamp_sms_message() == "Thank you! Your order was placed and will be delivered before 18:52" 
"""

```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# Takeaway class unit tests
from lib.customer import *

"""
given a customer instance
where customer has selected multiple dishes
add_customer_order adds all customer order to self.all_customer_orders
"""
def test_add_customer_order_adds_all_customer_order():
    customer = Mock()
    customer.name = "John Mayer"
    customer.address =  "71 Mayfair Street"
    customer.phone = "123456789101"

    customer.add_dish("Burger", 1)
    customer.add_dish("fries", 1)

    takeaway = Takeaway()
    takeaway.add_customer_order(customer)
    assert takeaway.all_customer_orders == {"John Mayer" : [{"dish name" : "burger", "price" : 5.80, "quantity": 1}, {"dish name" : "fries", "price" : 1.80, "quantity": 1}]}


"""
verify_order() shows the itemised receipt
"""
def test_verify_order_shows_the_itemised_receipt():
    customer = Customer("John Mayer", "71 Mayfair Street", "123456789101")
    customer.add_dish("Burger", 1)
    customer.add_dish("Fries", 1)

    takeaway = Takeaway()
    takeaway.add_customer_order(customer)
    assert takeaway.verify_order() == "Food     Qty     Price\nBurger     1     1.50\nFries    1     1.80\nTotal     7.60"



"""
given a customer instance
where customer has selected the dishes
add_customer_order has added the customer order to self.all_customer_orders
generate_timestamp_sms_message() generates sms message
"""
def test_generate_timestamp_sms_message_generatates_sms_message():
    customer = Mock()
    customer.name = "John Mayer"
    customer.address =  "71 Mayfair Street"
    customer.phone = "123456789101"

    customer.add_dish("Burger", 1)
    customer.add_dish("Fries", 1)

    takeaway = Takeaway()
    takeaway.add_customer_order(customer)
    takeaway.generate_timestamp_sms_message() #=> "Thank you! Your order was placed and will be delivered before 18:52" #18:52 is an example only 



#Customer class unit test
from unittest.mock import Mock
import pytest

"""
given a name, address, phone 
should initialize name, address and phone
"""
def test_given_name_address_phone_should_initialize_these_properties():
    customer = Customer("John Mayer", "71 Mayfair Street", "123456789101")
    assert customer.name == "John Mayer"
    assert customer.address ==  "71 Mayfair Street"
    assert customer.phone == "123456789101"


"""
given a takeaway instance
view_menu() returns the menu in string format
"""
def test_given_takeaway_instance_returns_menu():
    customer = Customer("John Mayer", "71 Mayfair Street", "123456789101")
    takeaway = Takeaway()

    assert customer.view_menu(takeaway) == "burger, price : 5.80\nfries, price : 1.80\npizza, price : 9\nhalloumi fries, price : 7\nsirloin steak, price: 16.99"


"""
add_dish without quantity adds dish to customer selected list with a quantity of 1
note: quantity is an optional parameter with a default value of 1
"""
def test_given_dish_without_quantity_adds_dish_with_quantity_of_1():
    customer = Customer("John Mayer", "71 Mayfair Street", "123456789101")
    customer.add_dish("halloumi fries")
    assert customer.customer_selected_dishes == [{"dish name":"halloumi fries", "price": 4, "qty": 1}]


"""
multiple same add_dish without quantity adds dish to customer selected list and increases quantity as necessary
"""
def test_given_same_dish_without_quantity_adds_dish_with_necessary_quantity():
    customer = Customer("John Mayer", "71 Mayfair Street", "123456789101")
    customer.add_dish("halloumi fries")
    customer.add_dish("halloumi fries")
    assert customer.customer_selected_dishes == [{"dish name":"halloumi fries", "price": 4, "qty": 2}]


"""
multiple different add_dish without quantity adds different dish to customer selected list with a quantity of 1
"""
def test_given_different_dish_without_quantity_adds_dish_with_quantity_of_1():
    customer = Customer("John Mayer", "71 Mayfair Street", "123456789101")
    customer.add_dish("halloumi fries")
    customer.add_dish("fries")
    assert customer.customer_selected_dishes == [{"dish name":"halloumi fries", "price": 4, "qty": 1}, {"dish name":"fries", "price": 1.80, "qty": 1}]


"""
add_dish with quantity adds dish to customer selected list with the given quantity
"""
def test_given_dish_with_quantity_adds_dish_with_given_quantity():
    customer = Customer("John Mayer", "71 Mayfair Street", "123456789101")
    customer.add_dish("halloumi fries", 2)
    assert customer.customer_selected_dishes #=> [{"dish name":"halloumi fries", "price": 4, "qty": 2}]


"""
multiple add_dish with quantity adds multiple dish to customer selected list with the given quantity
"""
def test_given_dish_with_quantity_adds_multiple_dish_with_given_quantity():
    customer = Customer("John Mayer", "71 Mayfair Street", "123456789101")
    customer.add_dish("halloumi fries", 2)
    customer.add_dish("sirloin steak", 2)
    assert customer.customer_selected_dishes == [{"dish name":"halloumi fries", "price": 4, "qty": 2}, {"dish name":"sirlion steak", "price": 16.99, "qty": 2}]


"""
given if food is not on the menu
add_dish() raises error message "food not in the menu!"
add_dish() only adds dish that is in the menu
"""
def test_given_dish_is_not_on_menu_returns_error_and_only_adds_dish_that_is_in_the_menu():
    customer = Customer("John Mayer", "71 Mayfair Street", "123456789101")
    customer.add_dish("halloumi fries", 2)

    with pytest.raises(ValueError) as e:
        customer.add_dish("grilled salmon", 2) 
    
    assert str(e.value) == "food not in the menu!"
    assert customer.customer_selected_dishes == [{"dish name":"halloumi fries", "price": 4, "qty": 2}]


"""
given an empty food parameter
add_dish() raises error message "Food cannot be empty!"
"""
def test_given_empty_food_parameter_raises_error():
    customer = Customer("John Mayer", "71 Mayfair Street", "123456789101")
    from pytest.raises(ValueError) as e:
        customer.add_dish("") 
    
    assert str(e.value) == "Food cannot be empty!"


"""
given a specified dish without quantity
remove_dish() removes specified dish if found in selected list
note: quantity is an optional parameter with a default value of 1
"""
def test_given_dish_without_quantity_remove_dish_removes_dish_if_found_in_selected_list():
    customer = Customer("John Mayer", "71 Mayfair Street", "123456789101")
    customer.add_dish("halloumi fries")
    customer.remove_dish("halloumi fries")
    assert customer.customer_selected_dishes == []


"""
given a specified dish without quantity
remove_dish() throws error message if food not found in the menu or not in selected list
"""
def test_given_dish_without_quantity_throws_error_if_food_not_in_selected_list():
    customer = Customer("John Mayer", "71 Mayfair Street", "123456789101")
    customer.add_dish("halloumi fries")
    customer.remove_dish("curly fries")
    assert customer.customer_selected_dishes == "Food not found. So cannot be removed"


"""
given a specified dish with quantity
remove_dish() removes the dish and corrects the quantity
"""
def test_given_dish_with_quantity_removes_dish_and_corrects_quantity():
    customer = Customer("John Mayer", "71 Mayfair Street", "123456789101")
    customer.add_dish("halloumi fries", 3)
    customer.remove_dish("halloumi fries", 2)
    assert customer.customer_selected_dishes == [{"dish name":"halloumi fries", "price": 4, "qty": 1}]


"""
given a specified dish with quantity more than what is in the selected_dish list
remove_dish() delete the specified dish
"""
def test_given_specified_dish_with_quantity_more_than_what_is_in_the_selected_list_removes_item():
    customer = Customer("John Mayer", "71 Mayfair Street", "123456789101")
    customer.add_dish("halloumi fries", 3)
    customer.remove_dish("halloumi fries", 4)
    assert customer.customer_selected_dishes == []

```
