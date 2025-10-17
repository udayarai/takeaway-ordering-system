class Takeaway: #Main class
    # User-facing properties:
    #   None

    def __init__():
        # Parameters:
        #   None
        # Self instance variable:
        #   self.all_customer_orders = [] #list that stores all customer_orders
        #   for e.g. [{customer1 : [{"dish name" : "burger", "price" : 5.80, "quantity": 1}, {"dish name" : "fries", "price" : 1.80, "quantity": 1}]
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

    def generate_timestamp_sms_message(self):
        # Parameters:
        #   None
        # Returns:
        #   Sends sms message to the customer using vonage package
        pass # No code here yet