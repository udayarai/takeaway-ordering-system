from datetime import datetime

class Takeaway: #Main class
    # User-facing properties:
    #   None

    def __init__(self):
        # Parameters:
        #   None
        # Self instance variable:
        self.all_customer_orders = {} #list that stores all customer_orders as dictionary
        #   for e.g. {customer1 : [{"dish name" : "burger", "price" : 5.80, "quantity": 1}, {"dish name" : "fries", "price" : 1.80, "quantity": 1}]
        pass # No code here yet

    def get_menu(self):
        #Returns
        #   returns a list with dictionaries for e.g. see below
        menu_list =  [
            {"dish name" : "burger", "price" : 5.80}, 
            {"dish name": "fries", "price" : 1.80},
            {"dish name": "pizza", "price" : 9},
            {"dish name": "halloumi fries", "price" : 7},
            {"dish name": "sirloin steak", "price" : 16.99}
            ]
        return menu_list

    def add_customer_order(self, customer):
        # Parameters:
        #   customer: an instance of Customer
        # Side-effects:
        #   Adds the customer order to self.all_customer_orders of the self object
        self.all_customer_orders[customer.name] = customer.customer_selected_dishes

    def verify_order(self, customer):
        # Parameters:
        #   customer: an instance of Customer
        # Returns:
        #   An itemised recipt with total
        #   for e.g.
        #   Food    Qty Price 
        #   Burger  1   1.50
        #   Pizza   2   2
        #
        #   Total   3.50

        total = 0
        output = "Food\tQty\tPrice\n"

        for order in self.all_customer_orders[customer.name]: #key customer.name has list where individual items are dict inside that list
            print(order)
            total += order["price"]
            output += f"{order['dish name']}\t{order['quantity']}\t{order['price']:.2f}\n"
        
        output += f"Total\t\t{total:.2f}"
        return output.rstrip("\n")

    def generate_timestamp_sms_message(self):
        # Parameters:
        #   None
        # Returns:
        #   String with message "Thank you! Your order was placed and will be delivered before 18:52" 
        order_date_time_object = datetime.now()
        time_needed_for_delivery = 1    #hour
        hour = order_date_time_object.hour + time_needed_for_delivery #add 1 hr to hour
        mins = order_date_time_object.minute
        
        return f"Thank you! Your order was placed and will be delivered before {hour}:{mins}"

    def send_sms_message(self):
        # Parameters:
        #   None
        # Returns:
        #   Sends sms message to the customer using vonage package
        pass # No code here yet