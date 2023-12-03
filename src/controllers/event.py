from settings.config import constants, queries
from utils.uuid_generator import generate_uuid
from models.database import DBConnection


class Event:
   
    def __init__(self, **event_details: dict) -> None:
        self.event_id = generate_uuid()
        self.user_id = event_details.get('user_id')
        self.event_name = event_details.get('event_name')
        self.event_date = event_details.get('event_date')
        self.location = event_details.get('location')
        self.rating = event_details.get('rating')
        self.price = event_details.get('price')
        self.category = event_details.get('category')
        self.ticket_quantity = event_details.get('ticket_quantity')
        self.db = DBConnection()
        
    
    def add_event(self) ->None:
        '''Method to add event in the events table'''
        
        event_details = (
            self.event_id,
            self.user_id,
            self.event_name,
            self.event_date,
            self.location,
            self.rating,
            self.price,
            self.category,
            self.ticket_quantity
            )
        self.db.insert_item(queries["INSERT_EVENT"], event_details)      
       
              
        
    def remove_event(self) -> None:
        '''Method to remove event in the events table'''
    
        self.db.delete_item(queries["DELETE_EVENT"], (self.user_id, self.event_name))
        
          
    def get_event_by_user(self):
        '''Mehod to get the events added by a specific manager'''
        
        return self.db.get_item(queries["SEARCH_EXISTING_EVENT"], (self.user_id, self.event_name,))
        
    def get_event(self):
        '''Method to get all the events present in the the event table'''
        
        return self.db.get_item(queries["SEARCH_EVENT"],  self.event_name)
        
        
    def list_all_events(self) ->list:
        '''Method to list overall events from the events table'''
        
        return self.db.get_all_events(queries["LIST_EVENTS"])

    
    def list_events(self) ->tuple:
        '''Method to list the events particular to a manager for the manager itself'''
        
        return self.db.get_items(queries["LIST_USER_EVENTS"], (self.user_id,))
        
        
        
    def book_event(self, booked_event_details) ->None:
        '''Method to book the event for customer'''
        
        self.db.insert_item(queries["INSERT_BOOKING"], booked_event_details)
        return True   
            
    def get_ticket_qty(self):
        '''Method to get the ticket quantity of a particular event'''
        
        return self.db.get_item(queries["GET_TICKET_QTY"], self.event_name)
    
    
    def update_ticket(self, updated_ticket_qty, event_id) ->None:
        '''Method to update the tickets of the event which is booked'''

        self.db.update_item(queries["UPDATE_TICKET_QTY"], (updated_ticket_qty, event_id))
        
              
    def filter_event(self, filter_type: str, filter_value: str) ->list:
        '''Method to filter the events by a specific condition'''
        
        if filter_type == "rating":
            return self.db.get_items(queries["FILTER_RATING"], (filter_value,))
        elif filter_type == "price":
            return self.db.get_items(queries["FILTER_PRICE"], (filter_value,))
        elif filter_type == "category":
            return self.db.get_items(queries["FILTER_CATEGORY"], (filter_value,))
        elif filter_type == "location":
            return self.db.get_items(queries["FILTER_LOCATION"], (filter_value,))

       
    def search_event(self, partial_name: str) ->list:
        '''Method to search the event by entering name partially or completely'''
        
        partial_name = f"%{partial_name}%"
        return self.db.get_items(queries["SEARCH_BY_EVENT_NAME"], (partial_name,))
        

    def update_event(self, choice, eventname, new_event_name=None, new_event_date=None,
                     new_event_rating=None, new_event_price=None, new_event_category=None) ->None:
        '''Method to update the event details by the manager'''
    
        if choice == constants["ONE"]:
            self.db.update_item(queries["UPDATE_EVENT_NAME"], (new_event_name, eventname, self.user_id))
            return True
        elif choice == constants["TWO"]:
            self.db.update_item(queries["UPDATE_EVENT_DATE"], (new_event_date, eventname, self.user_id))
            return True
        elif choice == constants["THREE"]:
            self.db.update_item(queries["UPDATE_EVENT_RATING"], (new_event_rating,eventname, self.user_id))
            return True 
        elif choice == constants["FOUR"]:
            self.db.update_item(queries["UPDATE_EVENT_PRICE"], (new_event_price, eventname, self.user_id))
            return True    
        elif choice == constants["FIVE"]:
            self.db.update_item(queries["UPDATE_EVENT_CATEGORY"], (new_event_category, eventname, self.user_id))
            return True