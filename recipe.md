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
        #   for e.g. [{customer1 : [{"dish name" : "burger", "price" : 5.80, "quantity": 1}, {"dish name" : "fries", "price" : 1.80, "quantity": 1}]

    def get_menu(self):
        #Returns
        #   returns a list with dictionaries for e.g. see below
        #   [{"dish_name" : "burger", "price" : 5.80}, {"dish_name": "fries", "price" : 1.80}]

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

    def generate_timestamp_sms_message(self):
        # Parameters:
        #   None
        # Returns:
        #   Sends sms message to the customer using vonage package

class Customer:
    # User-facing properties:
    #   name: string
    #   address: string
    #   phone: string

    def __init__(self, name, address, phone):
        # Parameters:
        # name: string
        # address: string
        # phone: string
        # Side-effects:
        #   Sets the name, address and phone of the customer
        #self.name = name
        #self.address = address
        #self.phone = phone
        #
        # Class instance variable
        #   self.customer_selected_dishes = []  #list to store customer selected dishes
        #   for e.g. [{"dish name":"burger", "price": 4, "qty": 1}, ...]
        pass # No code here yet


    def view_menu(self, takeaway):
        #Parameters:
        #   takeaway : an instance of object Takeaway
        #Returns
        #   returns a string of food names and prices
        #   "burger", "price" : 5.80
        #   "fries", "price" : 1.80
        pass # No code here yet

    def add_dish(self, dish, quantity):
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

    def format(self):
        # Returns:
        #   A string of the form "TITLE by ARTIST"
        pass # No code here yet

```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMPLE

"""
Given a library
When we add two tracks
We see those tracks reflected in the tracks list
"""
library = MusicLibrary()
track_1 = Track("Carte Blanche", "Veracocha")
track_2 = Track("Synaesthesia", "The Thrillseekers")
library.add(track_1)
library.add(track_2)
library.tracks # => [track_1, track_2]
```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE

"""
Given a track with a title and an artist
We see the title reflected in the title property
"""
track = Track("Carte Blanche", "Veracocha")
track.title # => "Carte Blanche"
```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
