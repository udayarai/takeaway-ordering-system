from lib.customer import *
from lib.takeaway import *
from unittest.mock import Mock

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
    customer.customer_selected_dishes = [{"dish name" : "burger", "price" : 5.80, "quantity": 1}, {"dish name" : "fries", "price" : 1.80, "quantity": 1}]

    takeaway = Takeaway()
    takeaway.add_customer_order(customer)
    assert takeaway.all_customer_orders == {"John Mayer" : [{"dish name" : "burger", "price" : 5.80, "quantity": 1}, {"dish name" : "fries", "price" : 1.80, "quantity": 1}]}


"""
verify_order() shows the itemised receipt
"""
def test_verify_order_shows_the_itemised_receipt():
    customer = Mock
    customer.name = "John Mayer"
    customer.address =  "71 Mayfair Street"
    customer.phone = "123456789101"
    
    customer.customer_selected_dishes = [{"dish name" : "burger", "price" : 5.80, "quantity": 1}, {"dish name" : "fries", "price" : 1.80, "quantity": 1}]

    takeaway = Takeaway()
    takeaway.add_customer_order(customer)
    assert takeaway.verify_order(customer) == "Food\tQty\tPrice\nburger\t1\t5.80\nfries\t1\t1.80\nTotal\t\t7.60"



"""
given a customer instance
where customer has selected the dishes
add_customer_order has added the customer order to self.all_customer_orders
generate_timestamp_sms_message() generates sms message
"""
from unittest.mock import Mock
from lib.takeaway import Takeaway

def test_generate_timestamp_sms_message_generatates_sms_message():
    # Mock the Vonage client class and its instance
    mock_client_class = Mock()
    mock_vonage_instance = Mock()
    mock_sms = Mock()
    mock_response = Mock()

    # Setup the response from sms.send()
    mock_response.model_dump.return_value = {
        "messages": [{"status": "0"}]
    }
    mock_sms.send.return_value = mock_response

    # Link mocks together
    mock_vonage_instance.sms = mock_sms
    mock_client_class.return_value = mock_vonage_instance

    # Create customer mock
    customer = Mock()
    customer.phone = "07828906675"

    # Create instance of Takeaway
    takeaway = Takeaway()

    # Call send_sms_message with mocked Vonage client class
    result = takeaway.send_sms_message("your message has been delivered", customer, mock_client_class)

    # Assert success message
    assert result == "Message sent successfully."



