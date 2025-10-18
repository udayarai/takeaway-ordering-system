from lib.takeaway import * 

class Customer:
    # User-facing properties:
    #   name: string
    #   address: string
    #   phone: string

    def __init__(self, name, address, phone, takeaway):
        # Parameters:
        # name: string
        # address: string
        # phone: string
        # takeaway: object instance of Takeaway class
        # Side-effects:
        #   Sets the name, address and phone of the customer
        self.name = name
        self.address = address
        self.phone = phone
        self.takeaway = takeaway
        #
        # Class instance variable
        self.customer_selected_dishes = []  #list to store customer selected dishes
        #   for e.g. [{"dish name":"burger", "price": 4, "qty": 1}, ...]


    def view_menu(self):
        #Parameters:
        #   None
        #Returns menu in string format
        #   for e.g. halloumi fries, price: 7 etc
        menu_list = self.takeaway.get_menu()
        output = []

        for item in menu_list:
            output.append(f"{item['dish name']}, price:{item['price']:.2f}")
        
        return "\n".join(output)
        
    
    def add_dish(self, dish, quantity=1):
        #Parameters:
        #   dish: string representing name of dish for e.g. burger
        #   quantity: integer representing quantity of dish e.g. 1, 2, 3, etc
        # Side-effects:
        #   Adds the customer selected dishes to self.customer_selected_dishes of the self object
        menu_list = self.takeaway.get_menu()

        #check dish parameter is not empty
        if not dish:
            raise ValueError("Food cannot be empty!")

        #check dish is in menu
        dish_in_menu = next((item for item in menu_list if item["dish name"]== dish), None) #returns item dict if in dish else returns None
        if not dish_in_menu: #if dish_in_menu is None
            raise ValueError("food not in the menu!")
        
        #check dish is already in selected
        if len(self.customer_selected_dishes) > 0:                        #only run duplicate check if list is not empty
            for each_selected_dish in self.customer_selected_dishes:      #loop through selected dish
                if each_selected_dish["dish name"] == dish:   #if dish is already in selected    
                    each_selected_dish["quantity"] +=  quantity     #update the quantity 
                    return None
                
        #if its not in selected
        self.customer_selected_dishes.append({"dish name" : dish, "price" : dish_in_menu["price"], "quantity" : quantity})



    def remove_dish(self, dish, quantity=1):
        #Parameters:
        #   dish: string representing name of dish for e.g. burger
        #   quantity (optional default=1): integer representing quantity of dish e.g. 1, 2, 3, etc
        # Side-effects:
        #   Removes the customer selected dishes from self.customer_selected_dishes of the self object
        menu_list = self.takeaway.get_menu()

        #check if dish is in menu list
        dish_in_menu_list = next((item for item in menu_list if item["dish name"] == dish), None)

        if not dish_in_menu_list:
            raise ValueError("Food not found. So cannot be removed")
        
        #check if dish is in selected list
        dish_in_selected_list = next((item for item in self.customer_selected_dishes if item["dish name"] == dish), None)

        if not dish_in_selected_list:   #if selected_list empty
            raise ValueError("Food not found. So cannot be removed")
            
        #dish in selected list
        if quantity < dish_in_selected_list["quantity"]:
            dish_in_selected_list["quantity"] -= quantity
        else:       #if quantity is equal or greater than selected list quantity remove the item completely
            self.customer_selected_dishes.remove(dish_in_selected_list) #remove selected dish from selected dishes list
        

# takeaway = Takeaway()
# customer = Customer("John Mayer", "71 Mayfair Street", "123456789101", takeaway)
# customer.add_dish("halloumi fries")
# customer.add_dish("fries")
# print(customer.customer_selected_dishes)