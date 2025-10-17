# Takeaway class Integration tests
from lib.customer import *
from lib.takeaway import *

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