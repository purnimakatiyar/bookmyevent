from settings.config import prompts, constants
from controllers.user import User
from controllers.authentication import Authenticate
from helpers.validators import is_valid_username, is_valid_password, is_valid_name, is_valid_phone, validate_event_name, validate_event_date, validate_event_price, validate_event_tickets, check_valid_password
from dateutil import parser
from controllers.event import Event
from controllers.booked_events import BookedEvents
import maskpass


class Input:
    
    
    def login_input(self):
        username = input(prompts["AUTH_USERNAME"])
        password = maskpass.advpass()
        auth = Authenticate(username, password)
        details =  (username, auth.login())
        if details[1] is not None:
            return details
        else:
            return False
        
    
    def get_valid_input(self, prompt, validation_function):
        while True:
            user_input = input(prompt)
            if validation_function(user_input):
                return user_input
            else:
                print(prompts["INVALID_INPUT"])
         
                
    def signup_input(self, user_role):
        user = User(
        username = self.get_valid_input(prompts["USERNAME"], is_valid_username),
        password = check_valid_password(maskpass.advpass()),
        name = self.get_valid_input(prompts["NAME"], is_valid_name),
        phone = self.get_valid_input(prompts["PHONE"], is_valid_phone),
        user_role = user_role
        )
        user.signup(user_role)
        
        
    def remove_manager_input(self):
        username = input(prompts["DELETE_MANAGER"])
        user = User()
        user.remove_manager(username)


    def add_event_input(self, username):
        event_name = self.get_valid_input(prompts["EVENT_NAME"], validate_event_name)
        input_date = self.get_valid_input(prompts["EVENT_DATE"], validate_event_date)
        event = Event(
            user_id  = User().get_user_id(username),
            event_name = event_name,
            event_date = parser.parse(input_date).strftime('%Y-%m-%d'),
            location = input(prompts["EVENT_LOCATION"]),
            price = self.get_valid_input(prompts["EVENT_PRICE"], validate_event_price),
            category = input(prompts["EVENT_CATEGORY"]),
            ticket_quantity = self.get_valid_input(prompts["EVENT_TICKETS"], validate_event_tickets)
        )
        event.add_event()

    
    def remove_event_input(self, username):
        event = Event(user_id = User().get_user_id(username),event_name = input(prompts["REMOVE_EVENT"]),)
        event.remove_event()
        
    def list_event_input(self, username):
        user_id = User().get_user_id(username),
        event = Event()
        event.list_events(user_id)
        
        
    def view_event_input(self):
        event = Event(event_name = input(prompts["VIEW_EVENT"]),)
        event.view_event()
        
        
    def book_event_input(self, username):
        event = Event(
        user_id = User().get_user_id(username),
        event_name = input(prompts["BOOK_EVENT"]),
        ticket_quantity = int(input(prompts["BOOK_EVENT_TICKETS"]))
        )
        event.book_event()
        
    def view_booked_event_input(self, username):
        user_id = User().get_user_id(username)
        booked_event = BookedEvents()
        booked_event.view_booked_events(user_id)
        
        
    def filter_event_input(self):
        event = Event()
        filter_type = input(prompts["FILTER_TYPE"])
        filter_value = input(prompts["FILTER_VALUE"])
        event.filter_event(filter_type, filter_value)
        
    def search_event_input(self):
        event = Event()
        partial_name = input(prompts["PARTIAL_EVENT_NAME"])
        event.search_event(partial_name)
        
    
    def update_event_input(self, username, choice, existing_event_name=None, new_event_name=None, new_event_date=None,
                           new_event_rating=None, new_event_price=None, new_event_category=None):
        event = Event(user_id = User().get_user_id(username),)
        
        if existing_event_name is None:
            existing_event_name = input(prompts["EXISTING_EVENT_NAME"])

        if choice in constants.values():
            if choice == constants["ONE"] and new_event_name is None:
                new_event_name = input(prompts["NEW_EVENT_NAME"])
                
            elif choice == constants["TWO"] and new_event_date is None:
                new_event_date = input(prompts["NEW_EVENT_DATE"])
                
            elif choice == constants["THREE"] and new_event_rating is None:
                new_event_rating = input(prompts["NEW_EVENT_RATING"])
                
            elif choice == constants["FOUR"] and new_event_price is None:
                new_event_price = input(prompts["NEW_EVENT_PRICE"])
                
            elif choice == constants["FIVE"] and new_event_category is None:
                new_event_category = input(prompts["NEW_EVENT_CATEGORY"])

            event.update_event(choice, existing_event_name, new_event_name, new_event_date,
                               new_event_rating, new_event_price, new_event_category)
        else:
            print(prompts["WRONG_INPUT"])