# Takeaway class unit tests
# from lib.customer import *
# from lib.takeaway import *
# from unittest.mock import Mock

# """
# given a customer instance
# where customer has selected multiple dishes
# add_customer_order adds all customer order to self.all_customer_orders
# """
# def test_add_customer_order_adds_all_customer_order():
#     customer = Mock()
#     customer.name = "John Mayer"
#     customer.address =  "71 Mayfair Street"
#     customer.phone = "123456789101"
#     customer.customer_selected_dishes.return_value = [{"dish name" : "burger", "price" : 5.80, "quantity": 1}, {"dish name" : "fries", "price" : 1.80, "quantity": 1}]

#     takeaway = Takeaway()
#     takeaway.add_customer_order(customer)
#     assert takeaway.all_customer_orders == {"John Mayer" : [{"dish name" : "burger", "price" : 5.80, "quantity": 1}, {"dish name" : "fries", "price" : 1.80, "quantity": 1}]}


# """
# verify_order() shows the itemised receipt
# """
# def test_verify_order_shows_the_itemised_receipt():
#     customer = Customer("John Mayer", "71 Mayfair Street", "123456789101")
#     customer.add_dish("Burger", 1)
#     customer.add_dish("Fries", 1)

#     takeaway = Takeaway()
#     takeaway.add_customer_order(customer)
#     assert takeaway.verify_order() == "Food     Qty     Price\nBurger     1     1.50\nFries    1     1.80\nTotal     7.60"



# """
# given a customer instance
# where customer has selected the dishes
# add_customer_order has added the customer order to self.all_customer_orders
# generate_timestamp_sms_message() generates sms message
# """
# def test_generate_timestamp_sms_message_generatates_sms_message():
#     customer = Mock()
#     customer.name = "John Mayer"
#     customer.address =  "71 Mayfair Street"
#     customer.phone = "123456789101"

#     customer.add_dish("Burger", 1)
#     customer.add_dish("Fries", 1)

#     takeaway = Takeaway()
#     takeaway.add_customer_order(customer)
#     takeaway.generate_timestamp_sms_message() #=> "Thank you! Your order was placed and will be delivered before 18:52" #18:52 is an example only 



