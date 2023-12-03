from settings.config import prompts, constants
from utils.input import Input
from controllers.user import User
from controllers.event import Event
from controllers.booked_events import BookedEvents
from utils.uuid_generator import generate_uuid
from utils.tableprint import list_event_table, booked_event_table


class EventHelper:
    
    def add_event(self, username) ->None:
        event_details = Input().add_event_input()
        user_id  = User().get_user_id(username)
        event = Event(
        user_id = user_id,
        event_name = event_details[0],
        event_date = event_details[1],
        location = event_details[2],
        price = event_details[3],
        category = event_details[4],
        ticket_quantity = event_details[5]
        )
        event.add_event()
        print(prompts["ADDED_EVENT"])
        
        
    def remove_event(self, username):
        event_name = Input().remove_event_input()
        user_id = User().get_user_id(username)
        event = Event(user_id = user_id, event_name = event_name)
        if event.get_event_by_user():
            event.remove_event()
            print(prompts["EVENT_REMOVED"])
        else:
            print(prompts["NO_EVENT_BY_USER"])
          
          
    def view_event(self):
        event_name = Input().view_event_input()
        event = Event(event_name = event_name)
        event_details = event.get_event()
        if event_details is None:
            print(prompts["EVENT_NOT_EXISTS"])
        else:
            print(f"""
                Event Name: {event_details[2]}
                Event Date: {event_details[3]}
                Location: {event_details[4]}
                Rating: {event_details[5]}
                Price: {event_details[6]}
                Category: {event_details[7]}
            """)
            
          
    def list_events(self, username):
        user_id = User().get_user_id(username)
        event = Event(user_id = user_id)
        events = event.list_events()
        if events is not None:
            
            list_event_table(events)
        else:
            print("No events found for the user.")
        
    def list_all_events(self):
        event = Event()
        events = event.list_all_events()
        list_event_table(events)
        
        
    def update_event(self, username, choice):
        event = Event(user_id = User().get_user_id(username))
        update_event_details = Input().update_event_input(choice)
        if event.update_event(update_event_details[0],update_event_details[1], 
                              update_event_details[2],update_event_details[3], 
                              update_event_details[4],update_event_details[5], 
                              update_event_details[6]):
            if choice == constants["ONE"]:
                print(prompts["CHANGED_EVENTNAME"])
            elif choice == constants["TWO"]:  
                print(prompts["CHANGED_EVENTDATE"])
            elif choice == constants["THREE"]:
                print(prompts["CHANGED_EVENTRATING"])
            elif choice == constants["FOUR"]:
                print(prompts["CHANGED_EVENTPRICE"])
            elif choice == constants["FIVE"]:
                print(prompts["CHANGED_EVENTCATEGORY"])
                
                
    def filter_event(self):
        filter_details = Input().filter_event_input()
        events = Event().filter_event(filter_details[0], filter_details[1])
        if events:
            list_event_table(events)
            return      
        else:
            print(prompts["NO_FILTER_EVENTS"])
            
            
    def search_event(self):
        partial_name = Input().search_event_input()
        event = Event()
        events = event.search_event(partial_name)
        if event:
            list_event_table(events)
        else:
            print(prompts["NO_FILTER_EVENTS"])
            
            
    def view_booked_event(self, username):
        user_id = User().get_user_id(username)
        booked_events = BookedEvents().view_booked_events(user_id)
        if booked_events:
            booked_event_table(booked_events)
            return
        else:
            print(prompts["NO_BOOKED_EVENTS"])
            
            
    def book_event(self, username) ->None:
        '''Method to book the event for customer'''
        user_id = User().get_user_id(username)
        book_event_details = Input().book_event_input()
        event_obj = Event(event_name = book_event_details[0])
        event = event_obj.get_event()
        if event is None:
            print(prompts["EVENT_NOT_EXISTS"])
            return
        else:
            if self.update_ticket(book_event_details[1], book_event_details[0]):
                booking_id = generate_uuid()
                booked_event_details = (booking_id, user_id, event[0], *book_event_details[0], event[3], book_event_details[1])
                if event_obj.book_event(booked_event_details):
                    print(prompts["BOOKED_EVENT"])
            
            
    def update_ticket(self, tickets , event_name) ->None:
        '''Method to update the tickets of the event which is booked'''
        event_obj = Event(event_name = event_name)
        current_ticket_qty = event_obj.get_ticket_qty()
        if current_ticket_qty is not None:
            if tickets > current_ticket_qty[0]:  
                print(prompts["TICKET_STATUS"])
            else:
                get_event_detail = event_obj.get_event()
                event_id = get_event_detail[1]
                updated_ticket_qty = current_ticket_qty[0] - tickets
                event_obj.update_ticket(updated_ticket_qty, event_id)
                return True
        else:
            print(prompts["NO_TICKETS"])