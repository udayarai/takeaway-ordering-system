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