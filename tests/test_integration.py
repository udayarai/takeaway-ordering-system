# Takeaway class Integration tests
from lib.customer import *
from lib.takeaway import *
import pytest


"""
given a customer instance
where customer has selected multiple dishes
add_customer_order adds all customer order to self.all_customer_orders
"""
pytest.mark.skip(reason="not ready yet")
def test_given_customer_instance_adds_all_customer_order():
    takeaway = Takeaway()
    customer = Customer("John Mayer", "71 Mayfair Street", "123456789101", takeaway)
    customer.add_dish("burger", 1)
    customer.add_dish("fries", 1)

    takeaway.add_customer_order(customer)
    assert takeaway.all_customer_orders == {"John Mayer" : [{"dish name" : "burger", "price" : 5.80, "quantity": 1}, {"dish name" : "fries", "price" : 1.80, "quantity": 1}]}


"""
given a customer instance
where customer has selected the dishes
add_customer_order has added the customer order to self.all_customer_orders
verify shows the itemised receipt with total
"""
pytest.mark.skip(reason="not ready yet")
def test_given_customer_instance_with_dishes_added_verify_order_shows_itemized_receipt():
    takeaway = Takeaway()
    customer = Customer("John Mayer", "71 Mayfair Street", "123456789101", takeaway)
    customer.add_dish("burger", 1)
    customer.add_dish("fries", 1)

    takeaway.add_customer_order(customer)
    assert takeaway.verify_order(customer) == "Food\tQty\tPrice\nburger\t1\t5.80\nfries\t1\t1.80\nTotal\t\t7.60"



"""
given a customer instance
where customer has selected the dishes
add_customer_order has added the customer order to self.all_customer_orders
generate_timestamp_sms_message() generates sms message
"""
@pytest.mark.skip(reason="not ready yet")
def test_generates_sms_message_with_timestamp():
    takeaway = Takeaway()
    customer = Customer("John Mayer", "71 Mayfair Street", "123456789101", takeaway)
    customer.add_dish("Burger", 1)
    customer.add_dish("Fries", 1)

    takeaway.add_customer_order(customer)
    takeaway.generate_timestamp_sms_message()
    assert takeaway.generate_timestamp_sms_message() == "Thank you! Your order was placed and will be delivered before 18:52" 