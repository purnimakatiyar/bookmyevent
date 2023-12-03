from settings.config import prompts, constants
from helpers.validators import is_valid_username, is_valid_name, is_valid_phone, validate_event_name, validate_event_date, validate_event_price, validate_event_tickets, check_valid_password
from dateutil import parser
import maskpass


class Input:
    
    
    def login_input(self):
        username = input(prompts["AUTH_USERNAME"])
        password = maskpass.advpass()
        auth_details = (username, password)
        return auth_details
        
    
    def get_valid_input(self, prompt, validation_function):
        while True:
            user_input = input(prompt)
            if validation_function(user_input):
                return user_input
            else:
                print(prompts["INVALID_INPUT"])
         
                
    def signup_input(self):
        username = self.get_valid_input(prompts["USERNAME"], is_valid_username)
        password = check_valid_password(maskpass.advpass())
        name = self.get_valid_input(prompts["NAME"], is_valid_name)
        phone = self.get_valid_input(prompts["PHONE"], is_valid_phone)
        return (username, password, name, phone)

           
    def remove_manager_input(self):
        return input(prompts["DELETE_MANAGER"])
        
    
    def add_event_input(self):
        event_name = self.get_valid_input(prompts["EVENT_NAME"], validate_event_name)
        input_date = self.get_valid_input(prompts["EVENT_DATE"], validate_event_date)
        event_date = parser.parse(input_date).strftime('%Y-%m-%d'),
        location = input(prompts["EVENT_LOCATION"]),
        price = self.get_valid_input(prompts["EVENT_PRICE"], validate_event_price),
        category = input(prompts["EVENT_CATEGORY"]),
        ticket_quantity = self.get_valid_input(prompts["EVENT_TICKETS"], validate_event_tickets)
        return (event_name, *event_date, *location, *price, *category, ticket_quantity)

    
    def remove_event_input(self):
        event_name = input(prompts["REMOVE_EVENT"])
        return event_name
        
    
    def view_event_input(self):
        event_name = input(prompts["VIEW_EVENT"])
        return event_name
        
        
    def book_event_input(self):
        event_name = input(prompts["BOOK_EVENT"]),
        ticket_quantity = int(input(prompts["BOOK_EVENT_TICKETS"]))
        return (event_name, ticket_quantity)
 
        
    def filter_event_input(self):
        while True:
            filter_type = input(prompts["FILTER_TYPE"])
            if filter_type not in ["rating", "price", "category", "location"]:
                print("Invalid filter type. Supported types: rating, price, category, location.")
                continue
            filter_value = input(prompts["FILTER_VALUE"])
            return (filter_type, filter_value)
        
        
    def search_event_input(self):
        partial_name = input(prompts["PARTIAL_EVENT_NAME"])
        return partial_name
        
    
    def update_event_input(self, choice):
        
        existing_event_name = input(prompts["EXISTING_EVENT_NAME"])
        new_event_name = None 
        new_event_date = None
        new_event_rating = None 
        new_event_price = None 
        new_event_category = None
        if choice == constants["ONE"]:
            new_event_name = input(prompts["NEW_EVENT_NAME"])
        elif choice == constants["TWO"] and new_event_date is None:
            new_event_date = input(prompts["NEW_EVENT_DATE"])
        elif choice == constants["THREE"] and new_event_rating is None:
            new_event_rating = input(prompts["NEW_EVENT_RATING"])  
        elif choice == constants["FOUR"] and new_event_price is None:
            new_event_price = input(prompts["NEW_EVENT_PRICE"])
        elif choice == constants["FIVE"] and new_event_category is None:
            new_event_category = input(prompts["NEW_EVENT_CATEGORY"])
        return (choice, existing_event_name, new_event_name, new_event_date,
                               new_event_rating, new_event_price, new_event_category)
        
            
    def update_account_input(self, choice):
        new_name = None
        new_password = None
        new_phone = None
        if choice == constants["ONE"]:
            new_password = maskpass.advpass()       
        elif choice == constants["TWO"]:
            new_name = input(prompts["NEW_NAME"])       
        elif choice == constants["THREE"]:
            new_phone = input(prompts["NEW_PHONE"])       
        return (choice, new_password, new_name, new_phone)