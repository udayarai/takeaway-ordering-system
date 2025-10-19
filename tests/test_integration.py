# Takeaway class Integration tests
from lib.customer import *
from lib.takeaway import *
from unittest.mock import Mock
from datetime import datetime
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
#@pytest.mark.skip(reason="not ready yet")
def test_generates_sms_message_with_timestamp():
    takeaway = Takeaway()
    customer = Customer("John Mayer", "71 Mayfair Street", "123456789101", takeaway)
    
    order_time = datetime.now()
    delivery_time = order_time.replace(hour = order_time.hour + 1)

    takeaway.add_customer_order(customer)
    assert takeaway.generate_timestamp_sms_message() == f"Thank you! Your order was placed and will be delivered before {delivery_time.strftime('%H:%M')}"


"""
given a customer instance
where customer has selected the dishes
add_customer_order has added the customer order to self.all_customer_orders
generate_timestamp_sms_message() has generated a sms message
send_sms_messages() sends sms_message given a correct phone number
"""
@pytest.mark.skip(reason="passed but manually skipped to stop running out of trial credit")
def test_send_sms_message_sends_sms_message():
    takeaway = Takeaway()
    customer = Customer("John Mayer", "71 Mayfair Street", "447828906673", takeaway)
    
    customer.add_dish("burger", 1)
    customer.add_dish("fries", 1)
    takeaway.add_customer_order(customer)
    takeaway.verify_order(customer)
    sms_message = takeaway.generate_timestamp_sms_message()
    assert takeaway.send_sms_message(sms_message, customer) == "Message sent successfully."
    