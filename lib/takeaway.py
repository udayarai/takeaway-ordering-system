from datetime import datetime
from vonage import Vonage, Auth, HttpClientOptions
from vonage_sms import SmsMessage
import cred

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
            #print(order)
            total += order["price"]
            output += f"{order['dish name']}\t{order['quantity']}\t{order['price']:.2f}\n"
        
        output += f"Total\t\t{total:.2f}"
        return output.rstrip("\n")

    def generate_timestamp_sms_message(self):
        # Parameters:
        #   None
        # Returns:
        #   String with message "Thank you! Your order was placed and will be delivered before 18:52" 
        order_time = datetime.now()
        delivery_time = order_time.replace(hour = order_time.hour + 1)
        
        return f"Thank you! Your order was placed and will be delivered before {delivery_time.strftime('%H:%M')}"

    def send_sms_message(self, sms_message, customer, client):  #pass Vonage in real production 
        # Parameters:
        #   customer: an instance of Customer
        # Returns:
        #   Sends sms message to the customer using vonage package
        
        #create an auth instance
        auth = Auth(api_key=cred.key, api_secret=cred.api_secret)

        # Create HttpClientOptions instance
        # (not required unless you want to change options from the defaults)
        options = HttpClientOptions(api_host='api.nexmo.com', timeout=30)

        # Create a Vonage instance
        vonage = client(auth=auth, http_client_options=options)

        message = SmsMessage(to=customer.phone, from_="Vonage", text=sms_message)
        response = vonage.sms.send(message)
        response_dict = response.model_dump()    #model_dump() converts response object to dict
        print(response_dict)

        if response_dict["messages"][0]["status"] == "0":
            return "Message sent successfully."
        else:
            return f"Message failed with error: {response_dict['messages'][0]['error-text']}"
        