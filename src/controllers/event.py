from settings.config import constants, queries, prompts
from utils.uuid_generator import generate_uuid
from utils.tableprint import list_event_table
from models.database import DBConnection
from utils import logs

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
        print(prompts["ADDED_EVENT"])
              
        
    def remove_event(self) -> None:
        '''Method to remove event in the events table'''
        
        event = self.db.get_item(queries["SEARCH_EXISTING_EVENT"], (self.event_name,))
        if event is None:
            print(prompts["EVENT_NOT_EXISTS"])
        else:
            self.db.delete_item(queries["DELETE_EVENT"], (self.user_id, self.event_name))
            event = self.db.get_item(queries["SEARCH_EXISTING_EVENT"], (self.event_name,))
            if event is not None:
                print(prompts["CANNOT_REMOVE_EVENT"])
            else:
                logs.remove_event(self.event_name)
                print(prompts["EVENT_REMOVED"])
            
        
    def view_event(self) -> tuple:
        '''Method to view a single event details'''
        
        event = self.db.get_item(queries["SEARCH_EVENT"], (self.event_name,))
        if event is None:
            print(prompts["EVENT_NOT_EXISTS"])
        else:
            print(f"""
                Event Name: {event[2]}
                Event Date: {event[3]}
                Location: {event[4]}
                Rating: {event[5]}
                Price: {event[6]}
                Category: {event[7]}
            """)
        
        
    def list_all_events(self) ->list:
        '''Method to list overall events from the events table'''
        
        events = self.db.get_all_events(queries["LIST_EVENTS"])
        list_event_table(events)
        return
    
    def list_events(self, user_id: str) ->tuple:
        '''Method to list the events particular to a manager for the manager itself'''
        
        events = self.db.get_events(queries["LIST_USER_EVENTS"], user_id)
        return list_event_table(events)
        
        
    def book_event(self) ->None:
        '''Method to book the event for customer'''
        
        event = self.db.get_item(
            queries["SEARCH_EXISTING_EVENT"],
            (self.event_name,)
        )
        if event is None:
            print(prompts["EVENT_NOT_EXISTS"])
            return
        
        if self.update_ticket(event):
            booking_id = generate_uuid()
            booked_event_details = (booking_id, self.user_id, event[0], self.event_name, event[3], self.ticket_quantity)
            if self.db.insert_item(queries["INSERT_BOOKING"], booked_event_details):
                print(prompts["BOOKED_EVENT"])
            
            
    def update_ticket(self, event) ->None:
        '''Method to update the tickets of the event which is booked'''
        
        current_ticket_qty = self.db.get_item(
            queries["GET_TICKET_QTY"],
            (self.event_name,)
        )[0]
        if current_ticket_qty is not None:
            if self.ticket_quantity > current_ticket_qty:  
                print(prompts["TICKET_STATUS"])
        
            get_event_detail = self.db.get_item(queries["SEARCH_EVENT"], (self.event_name,))
            if event is not None:
                event_id = get_event_detail[1]
                updated_ticket_qty = current_ticket_qty - self.ticket_quantity
                self.db.update_item(queries["UPDATE_TICKET_QTY"], (updated_ticket_qty, event_id))
                return True
        
              
    def filter_event(self, filter_type: str, filter_value: str) ->list:
        '''Method to filter the events by a specific condition'''
        
        if filter_type not in ["rating", "price", "category", "location"]:
            print("Invalid filter type. Supported types: rating, price, category, location")
            return
        if filter_type == "rating":
            events = self.db.get_items(queries["FILTER_RATING"], (filter_value,))
        elif filter_type == "price":
            events = self.db.get_items(queries["FILTER_PRICE"], (filter_value,))
        elif filter_type == "category":
            events = self.db.get_items(queries["FILTER_CATEGORY"], (filter_value,))
        elif filter_type == "location":
            events = self.db.get_items(queries["FILTER_LOCATION"], (filter_value,))

        if events:
            list_event_table(events)            
        else:
            print(prompts["NO_FILTER_EVENTS"])
    
    def search_event(self, partial_name: str) ->list:
        '''Method to search the event by entering name partially or completely'''
        
        partial_name = f"%{partial_name}%"
        events = self.db.get_items(queries["SEARCH_BY_EVENT_NAME"], (partial_name,))
        if events:
            list_event_table(events)
        else:
            print(prompts["NO_FILTER_EVENTS"])

    CHOICE_TO_QUERY_MAP = {
        constants["ONE"]: queries["UPDATE_EVENT_NAME"],
        constants["TWO"]: queries["UPDATE_EVENT_DATE"],
        constants["THREE"]: queries["UPDATE_EVENT_RATING"],
        constants["FOUR"]: queries["UPDATE_EVENT_PRICE"],
        constants["FIVE"]: queries["UPDATE_EVENT_CATEGORY"],
    }

    def update_event(self, choice, eventname, new_event_name=None, new_event_date=None,
                     new_event_rating=None, new_event_price=None, new_event_category=None) ->None:
        '''Method to update the event details by the manager'''
        
        if choice in self.CHOICE_TO_QUERY_MAP:
            query = self.CHOICE_TO_QUERY_MAP[choice]
        if choice == constants["ONE"]:
            self.db.update_item(query, (new_event_name, eventname, self.user_id))
            print(prompts["CHANGED_EVENTNAME"])
        elif choice == constants["TWO"]:
            self.db.update_item(query, (new_event_date, eventname, self.user_id))
            print(prompts["CHANGED_EVENTDATE"])
        elif choice == constants["THREE"]:
            self.db.update_item(query, (new_event_rating,eventname, self.user_id))
            print(prompts["CHANGED_EVENTRATING"])
        elif choice == constants["FOUR"]:
            self.db.update_item(query, (new_event_price, new_event_category, eventname, self.user_id))
            print(prompts["CHANGED_EVENTPRICE"])
        elif choice == constants["FIVE"]:
            self.db.update_item(query, (new_event_category, eventname, self.user_id))
            print(prompts["CHANGED_EVENTCATEGORY"])
        else:
            print(prompts["WRONG_INPUT"])